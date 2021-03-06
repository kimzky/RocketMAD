# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/grapeshot/grapeshot_uploading_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.grapeshot import grapeshot_chunk_data_pb2 as pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__chunk__data__pb2
from pogoprotos.data.grapeshot import grapeshot_compose_data_pb2 as pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__compose__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/grapeshot/grapeshot_uploading_data.proto',
  package='pogoprotos.data.grapeshot',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/data/grapeshot/grapeshot_uploading_data.proto\x12\x19pogoprotos.data.grapeshot\x1a\x34pogoprotos/data/grapeshot/grapeshot_chunk_data.proto\x1a\x36pogoprotos/data/grapeshot/grapeshot_compose_data.proto\"\xd0\x01\n\x16GrapeshotUploadingData\x12\x41\n\nchunk_data\x18\x01 \x03(\x0b\x32-.pogoprotos.data.grapeshot.GrapeshotChunkData\x12\x45\n\x0c\x63ompose_data\x18\x02 \x01(\x0b\x32/.pogoprotos.data.grapeshot.GrapeshotComposeData\x12\x12\n\ngcs_bucket\x18\x03 \x01(\t\x12\x18\n\x10number_of_chunks\x18\x04 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__chunk__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__compose__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GRAPESHOTUPLOADINGDATA = _descriptor.Descriptor(
  name='GrapeshotUploadingData',
  full_name='pogoprotos.data.grapeshot.GrapeshotUploadingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='pogoprotos.data.grapeshot.GrapeshotUploadingData.chunk_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compose_data', full_name='pogoprotos.data.grapeshot.GrapeshotUploadingData.compose_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gcs_bucket', full_name='pogoprotos.data.grapeshot.GrapeshotUploadingData.gcs_bucket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_chunks', full_name='pogoprotos.data.grapeshot.GrapeshotUploadingData.number_of_chunks', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=406,
)

_GRAPESHOTUPLOADINGDATA.fields_by_name['chunk_data'].message_type = pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__chunk__data__pb2._GRAPESHOTCHUNKDATA
_GRAPESHOTUPLOADINGDATA.fields_by_name['compose_data'].message_type = pogoprotos_dot_data_dot_grapeshot_dot_grapeshot__compose__data__pb2._GRAPESHOTCOMPOSEDATA
DESCRIPTOR.message_types_by_name['GrapeshotUploadingData'] = _GRAPESHOTUPLOADINGDATA

GrapeshotUploadingData = _reflection.GeneratedProtocolMessageType('GrapeshotUploadingData', (_message.Message,), dict(
  DESCRIPTOR = _GRAPESHOTUPLOADINGDATA,
  __module__ = 'pogoprotos.data.grapeshot.grapeshot_uploading_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.grapeshot.GrapeshotUploadingData)
  ))
_sym_db.RegisterMessage(GrapeshotUploadingData)


# @@protoc_insertion_point(module_scope)
