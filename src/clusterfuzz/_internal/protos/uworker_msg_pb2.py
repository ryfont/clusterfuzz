# Copyright 2020 Google LLC
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

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clusterfuzz/_internal/protos/uworker_msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.clusterfuzz/_internal/protos/uworker_msg.proto\x1a\x19google/protobuf/any.proto\"\x1a\n\x04Json\x12\x12\n\nserialized\x18\x01 \x01(\t\"3\n\x06\x45ntity\x12)\n\x0b\x61ny_wrapper\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"T\n\x14UworkerEntityWrapper\x12$\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x16\n\x07\x63hanged\x18\x02 \x01(\x0b\x32\x05.Json\"\x8b\x02\n\x1fUpdateFuzzerAndDataBundlesInput\x12\x1c\n\x06\x66uzzer\x18\x01 \x01(\x0b\x32\x07.EntityH\x00\x88\x01\x01\x12\x18\n\x0b\x66uzzer_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x0c\x64\x61ta_bundles\x18\x03 \x03(\x0b\x32\x07.Entity\x12\"\n\x15\x66uzzer_log_upload_url\x18\x04 \x01(\tH\x02\x88\x01\x01\x12 \n\x13\x66uzzer_download_url\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\t\n\x07_fuzzerB\x0e\n\x0c_fuzzer_nameB\x18\n\x16_fuzzer_log_upload_urlB\x16\n\x14_fuzzer_download_url\"\xb7\x05\n\x05Input\x12\x1e\n\x08testcase\x18\x01 \x01(\x0b\x32\x07.EntityH\x00\x88\x01\x01\x12.\n\x18testcase_upload_metadata\x18\x02 \x01(\x0b\x32\x07.EntityH\x01\x88\x01\x01\x12\x18\n\x0btestcase_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1f\n\x0buworker_env\x18\x04 \x01(\x0b\x32\x05.JsonH\x03\x88\x01\x01\x12\"\n\x15testcase_download_url\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08job_type\x18\x06 \x01(\tH\x05\x88\x01\x01\x12&\n\x19uworker_output_upload_url\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1d\n\x07variant\x18\x08 \x01(\x0b\x32\x07.EntityH\x07\x88\x01\x01\x12\x1e\n\x11original_job_type\x18\t \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x66uzzer_name\x18\n \x01(\tH\t\x88\x01\x01\x12S\n$update_fuzzer_and_data_bundles_input\x18\x0b \x01(\x0b\x32 .UpdateFuzzerAndDataBundlesInputH\n\x88\x01\x01\x12\x18\n\x0bmodule_name\x18\x0c \x01(\tH\x0b\x88\x01\x01\x42\x0b\n\t_testcaseB\x1b\n\x19_testcase_upload_metadataB\x0e\n\x0c_testcase_idB\x0e\n\x0c_uworker_envB\x18\n\x16_testcase_download_urlB\x0b\n\t_job_typeB\x1c\n\x1a_uworker_output_upload_urlB\n\n\x08_variantB\x14\n\x12_original_job_typeB\x0e\n\x0c_fuzzer_nameB\'\n%_update_fuzzer_and_data_bundles_inputB\x0e\n\x0c_module_name\"\xc3\x03\n\x0e\x46uzzTaskOutput\x12\x18\n\x0b\x66uzzer_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x63rash_revision\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11job_run_timestamp\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x1c\n\x0fnew_crash_count\x18\x04 \x01(\x03H\x03\x88\x01\x01\x12\x1e\n\x11known_crash_count\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12\x1f\n\x12testcases_executed\x18\x06 \x01(\x03H\x05\x88\x01\x01\x12#\n\x0fjob_run_crashes\x18\x07 \x01(\x0b\x32\x05.JsonH\x06\x88\x01\x01\x12(\n\x1b\x66ully_qualified_fuzzer_name\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\x0e\n\x0c_fuzzer_nameB\x11\n\x0f_crash_revisionB\x14\n\x12_job_run_timestampB\x12\n\x10_new_crash_countB\x14\n\x12_known_crash_countB\x15\n\x13_testcases_executedB\x12\n\x10_job_run_crashesB\x1e\n\x1c_fully_qualified_fuzzer_name\"\xc0\x04\n\x06Output\x12,\n\x08testcase\x18\x01 \x01(\x0b\x32\x15.UworkerEntityWrapperH\x00\x88\x01\x01\x12<\n\x18testcase_upload_metadata\x18\x02 \x01(\x0b\x32\x15.UworkerEntityWrapperH\x01\x88\x01\x01\x12+\n\x07variant\x18\x03 \x01(\x0b\x32\x15.UworkerEntityWrapperH\x02\x88\x01\x01\x12\x1e\n\x05\x65rror\x18\x04 \x01(\x0e\x32\n.ErrorTypeH\x03\x88\x01\x01\x12\"\n\ruworker_input\x18\x05 \x01(\x0b\x32\x06.InputH\x04\x88\x01\x01\x12\x19\n\x0ctest_timeout\x18\x06 \x01(\x02H\x05\x88\x01\x01\x12\x17\n\ncrash_time\x18\x07 \x01(\x02H\x06\x88\x01\x01\x12$\n\x17\x63rash_stacktrace_output\x18\x08 \x01(\tH\x07\x88\x01\x01\x12.\n\x10\x66uzz_task_output\x18\t \x01(\x0b\x32\x0f.FuzzTaskOutputH\x08\x88\x01\x01\x12\x1a\n\rerror_message\x18\n \x01(\tH\t\x88\x01\x01\x42\x0b\n\t_testcaseB\x1b\n\x19_testcase_upload_metadataB\n\n\x08_variantB\x08\n\x06_errorB\x10\n\x0e_uworker_inputB\x0f\n\r_test_timeoutB\r\n\x0b_crash_timeB\x1a\n\x18_crash_stacktrace_outputB\x13\n\x11_fuzz_task_outputB\x10\n\x0e_error_message*\xa7\x01\n\tErrorType\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x17\n\x13\x41NALYZE_BUILD_SETUP\x10\x01\x12\x14\n\x10\x41NALYZE_NO_CRASH\x10\x02\x12\x12\n\x0eTESTCASE_SETUP\x10\x03\x12\r\n\tUNHANDLED\x10\x04\x12\x17\n\x13VARIANT_BUILD_SETUP\x10\x05\x12!\n\x1dTESTCASE_SETUP_INVALID_FUZZER\x10\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clusterfuzz._internal.protos.uworker_msg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ERRORTYPE']._serialized_start=2246
  _globals['_ERRORTYPE']._serialized_end=2413
  _globals['_JSON']._serialized_start=77
  _globals['_JSON']._serialized_end=103
  _globals['_ENTITY']._serialized_start=105
  _globals['_ENTITY']._serialized_end=156
  _globals['_UWORKERENTITYWRAPPER']._serialized_start=158
  _globals['_UWORKERENTITYWRAPPER']._serialized_end=242
  _globals['_UPDATEFUZZERANDDATABUNDLESINPUT']._serialized_start=245
  _globals['_UPDATEFUZZERANDDATABUNDLESINPUT']._serialized_end=512
  _globals['_INPUT']._serialized_start=515
  _globals['_INPUT']._serialized_end=1210
  _globals['_FUZZTASKOUTPUT']._serialized_start=1213
  _globals['_FUZZTASKOUTPUT']._serialized_end=1664
  _globals['_OUTPUT']._serialized_start=1667
  _globals['_OUTPUT']._serialized_end=2243
# @@protoc_insertion_point(module_scope)