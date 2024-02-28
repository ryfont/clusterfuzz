# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for dealing with input and output (I/O) to a uworker."""

from typing import Tuple
from typing import Type
from typing import TypeVar
import uuid

from google.cloud import ndb
from google.cloud.datastore_v1.proto import entity_pb2
from google.cloud.ndb import model
import google.protobuf.message

from clusterfuzz._internal.base import task_utils
from clusterfuzz._internal.google_cloud_utils import storage
from clusterfuzz._internal.metrics import logs
from clusterfuzz._internal.protos import uworker_msg_pb2


def generate_new_input_file_name() -> str:
  """Generates a new input file name."""
  return str(uuid.uuid4()).lower()


def get_uworker_input_gcs_path() -> str:
  """Returns a GCS path for uworker I/O."""
  # Inspired by blobs.write_blob.
  io_bucket = storage.uworker_input_bucket()
  io_file_name = generate_new_input_file_name()
  if storage.get(storage.get_cloud_storage_file_path(io_bucket, io_file_name)):
    raise RuntimeError(f'UUID collision found: {io_file_name}.')
  return f'/{io_bucket}/{io_file_name}'


def get_uworker_output_urls(input_gcs_path: str) -> str:
  """Returns a signed download URL for the uworker to upload the output and a
  GCS url for the tworker to download the output. Make sure we can infer the
  actual input since the output is not trusted."""
  gcs_path = uworker_input_path_to_output_path(input_gcs_path)
  # Note that the signed upload URL can't be directly downloaded from.
  return storage.get_signed_upload_url(gcs_path), gcs_path


def uworker_input_path_to_output_path(input_gcs_path: str) -> str:
  return input_gcs_path.replace(storage.uworker_input_bucket(),
                                storage.uworker_output_bucket())


def uworker_output_path_to_input_path(output_gcs_path: str) -> str:
  return output_gcs_path.replace(storage.uworker_output_bucket(),
                                 storage.uworker_input_bucket())


def get_uworker_input_urls():
  """Returns a signed download URL for the uworker to download the input and a
  GCS url for the tworker to upload it (this happens first)."""
  gcs_path = get_uworker_input_gcs_path()
  return storage.get_signed_download_url(gcs_path), gcs_path


def upload_uworker_input(uworker_input: bytes, gcs_path: str):
  """Uploads input for the untrusted portion of a task."""
  storage.write_data(uworker_input, gcs_path)


def deserialize_uworker_input(
    serialized_uworker_input: bytes) -> uworker_msg_pb2.Input:
  """Deserializes input for the untrusted part of a task."""
  uworker_input_proto = uworker_msg_pb2.Input()
  uworker_input_proto.ParseFromString(serialized_uworker_input)
  return uworker_input_proto


def serialize_uworker_input(uworker_input: uworker_msg_pb2.Input) -> bytes:
  """Serializes and returns |uworker_input| as JSON. Can handle ndb entities."""
  return uworker_input.SerializeToString()


def serialize_and_upload_uworker_input(
    uworker_input: uworker_msg_pb2.Input) -> Tuple[str, str]:
  """Serializes input for the untrusted portion of a task."""
  signed_input_download_url, input_gcs_url = get_uworker_input_urls()
  # Get URLs for the uworker'ps output. We need a signed upload URL so it can
  # write its output. Also get a download URL in case the caller wants to read
  # the output.
  signed_output_upload_url, output_gcs_url = get_uworker_output_urls(
      input_gcs_url)

  assert not uworker_input.HasField('uworker_output_upload_url')
  uworker_input.uworker_output_upload_url = signed_output_upload_url

  serialized_uworker_input = uworker_input.SerializeToString()
  upload_uworker_input(serialized_uworker_input, input_gcs_url)

  return signed_input_download_url, output_gcs_url


def download_and_deserialize_uworker_input(
    uworker_input_download_url: str) -> uworker_msg_pb2.Input:
  """Downloads and deserializes the input to the uworker from the signed
  download URL."""
  data = storage.download_signed_url(uworker_input_download_url)
  return deserialize_uworker_input(data)


def serialize_uworker_output(
    uworker_output_obj: uworker_msg_pb2.Output) -> bytes:
  """Serializes uworker's output for deserializing by deserialize_uworker_output
  and consumption by postprocess_task."""
  return uworker_output_obj.SerializeToString()


def deserialize_uworker_output(serialized: bytes) -> uworker_msg_pb2.Output:
  output = uworker_msg_pb2.Output()
  try:
    output.ParseFromString(serialized)
  except google.protobuf.message.DecodeError:
    logs.log_error('Cannot decode uworker msg.')
    raise task_utils.UworkerMsgParseError('Cannot decode uworker msg.')
  return output


def serialize_and_upload_uworker_output(uworker_output: uworker_msg_pb2.Output,
                                        upload_url: str):
  """Serializes |uworker_output| and uploads it to |upload_url."""
  serialized_uworker_output = uworker_output.SerializeToString()
  storage.upload_signed_url(serialized_uworker_output, upload_url)


def download_input_based_on_output_url(
    output_url: str) -> uworker_msg_pb2.Input:
  input_url = uworker_output_path_to_input_path(output_url)
  serialized_uworker_input = storage.read_data(input_url)
  if serialized_uworker_input is None:
    logs.log_error(f'No corresponding input for output: {output_url}.')
  return deserialize_uworker_input(serialized_uworker_input)


def download_and_deserialize_uworker_output(
    output_url: str) -> uworker_msg_pb2.Output:
  """Downloads and deserializes uworker output."""
  serialized_uworker_output = storage.read_data(output_url)

  uworker_output = deserialize_uworker_output(serialized_uworker_output)

  # Now download the input, which is stored securely so that the uworker cannot
  # tamper with it.
  uworker_input = download_input_based_on_output_url(output_url)

  uworker_output.uworker_input.CopyFrom(uworker_input)
  return uworker_output


def entity_to_protobuf(entity: ndb.Model) -> entity_pb2.Entity:
  """Helper function to convert entity to protobuf format."""
  return model._entity_to_protobuf(entity)  # pylint: disable=protected-access


T = TypeVar('T', bound=ndb.Model)


def entity_from_protobuf(entity_proto: entity_pb2.Entity,
                         model_type: Type[T]) -> T:
  """Converts `entity_proto` to the `ndb.Model` of type `model_type` it encodes.

  Raises:
    AssertionError: if `entity_proto` does not encode a model of type
    `model_type`
  """
  entity = model._entity_from_protobuf(entity_proto)  # pylint: disable=protected-access
  assert isinstance(entity, model_type)
  return entity
