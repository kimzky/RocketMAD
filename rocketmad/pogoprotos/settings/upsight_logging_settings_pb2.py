# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/upsight_logging_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/upsight_logging_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/settings/upsight_logging_settings.proto\x12\x13pogoprotos.settings\"j\n\x16UpsightLoggingSettings\x12\x1b\n\x13use_verbose_logging\x18\x01 \x01(\x08\x12\x1a\n\x12logging_percentage\x18\x02 \x01(\x05\x12\x17\n\x0f\x64isable_logging\x18\x03 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPSIGHTLOGGINGSETTINGS = _descriptor.Descriptor(
  name='UpsightLoggingSettings',
  full_name='pogoprotos.settings.UpsightLoggingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_verbose_logging', full_name='pogoprotos.settings.UpsightLoggingSettings.use_verbose_logging', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logging_percentage', full_name='pogoprotos.settings.UpsightLoggingSettings.logging_percentage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disable_logging', full_name='pogoprotos.settings.UpsightLoggingSettings.disable_logging', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=75,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['UpsightLoggingSettings'] = _UPSIGHTLOGGINGSETTINGS

UpsightLoggingSettings = _reflection.GeneratedProtocolMessageType('UpsightLoggingSettings', (_message.Message,), dict(
  DESCRIPTOR = _UPSIGHTLOGGINGSETTINGS,
  __module__ = 'pogoprotos.settings.upsight_logging_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.UpsightLoggingSettings)
  ))
_sym_db.RegisterMessage(UpsightLoggingSettings)


# @@protoc_insertion_point(module_scope)
