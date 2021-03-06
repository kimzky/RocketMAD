# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/buddy_interaction_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/buddy_interaction_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n;pogoprotos/settings/master/buddy_interaction_settings.proto\x12\x1apogoprotos.settings.master\x1a\'pogoprotos/inventory/item/item_id.proto\"\x9a\x01\n\x18\x42uddyInteractionSettings\x12>\n\x13\x66\x65\x65\x64_item_whitelist\x18\x01 \x03(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12>\n\x13\x63\x61re_item_whitelist\x18\x02 \x03(\x0e\x32!.pogoprotos.inventory.item.ItemIdb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BUDDYINTERACTIONSETTINGS = _descriptor.Descriptor(
  name='BuddyInteractionSettings',
  full_name='pogoprotos.settings.master.BuddyInteractionSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feed_item_whitelist', full_name='pogoprotos.settings.master.BuddyInteractionSettings.feed_item_whitelist', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='care_item_whitelist', full_name='pogoprotos.settings.master.BuddyInteractionSettings.care_item_whitelist', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=133,
  serialized_end=287,
)

_BUDDYINTERACTIONSETTINGS.fields_by_name['feed_item_whitelist'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_BUDDYINTERACTIONSETTINGS.fields_by_name['care_item_whitelist'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['BuddyInteractionSettings'] = _BUDDYINTERACTIONSETTINGS

BuddyInteractionSettings = _reflection.GeneratedProtocolMessageType('BuddyInteractionSettings', (_message.Message,), dict(
  DESCRIPTOR = _BUDDYINTERACTIONSETTINGS,
  __module__ = 'pogoprotos.settings.master.buddy_interaction_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BuddyInteractionSettings)
  ))
_sym_db.RegisterMessage(BuddyInteractionSettings)


# @@protoc_insertion_point(module_scope)
