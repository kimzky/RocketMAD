# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/combat_ranking_settings.proto

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
  name='pogoprotos/settings/master/combat_ranking_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n8pogoprotos/settings/master/combat_ranking_settings.proto\x12\x1apogoprotos.settings.master\"\xf3\x02\n\x15\x43ombatRankingSettings\x12O\n\nrank_level\x18\x01 \x03(\x0b\x32;.pogoprotos.settings.master.CombatRankingSettings.RankLevel\x12Y\n\x14required_for_rewards\x18\x02 \x01(\x0b\x32;.pogoprotos.settings.master.CombatRankingSettings.RankLevel\x12\"\n\x1amin_rank_to_display_rating\x18\x03 \x01(\x05\x1a\x89\x01\n\tRankLevel\x12\x12\n\nrank_level\x18\x01 \x01(\x05\x12)\n!additional_total_battles_required\x18\x02 \x01(\x05\x12 \n\x18\x61\x64\x64itional_wins_required\x18\x03 \x01(\x05\x12\x1b\n\x13min_rating_required\x18\x04 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMBATRANKINGSETTINGS_RANKLEVEL = _descriptor.Descriptor(
  name='RankLevel',
  full_name='pogoprotos.settings.master.CombatRankingSettings.RankLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank_level', full_name='pogoprotos.settings.master.CombatRankingSettings.RankLevel.rank_level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_total_battles_required', full_name='pogoprotos.settings.master.CombatRankingSettings.RankLevel.additional_total_battles_required', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_wins_required', full_name='pogoprotos.settings.master.CombatRankingSettings.RankLevel.additional_wins_required', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_rating_required', full_name='pogoprotos.settings.master.CombatRankingSettings.RankLevel.min_rating_required', index=3,
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
  serialized_start=323,
  serialized_end=460,
)

_COMBATRANKINGSETTINGS = _descriptor.Descriptor(
  name='CombatRankingSettings',
  full_name='pogoprotos.settings.master.CombatRankingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank_level', full_name='pogoprotos.settings.master.CombatRankingSettings.rank_level', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_for_rewards', full_name='pogoprotos.settings.master.CombatRankingSettings.required_for_rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_rank_to_display_rating', full_name='pogoprotos.settings.master.CombatRankingSettings.min_rank_to_display_rating', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COMBATRANKINGSETTINGS_RANKLEVEL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=460,
)

_COMBATRANKINGSETTINGS_RANKLEVEL.containing_type = _COMBATRANKINGSETTINGS
_COMBATRANKINGSETTINGS.fields_by_name['rank_level'].message_type = _COMBATRANKINGSETTINGS_RANKLEVEL
_COMBATRANKINGSETTINGS.fields_by_name['required_for_rewards'].message_type = _COMBATRANKINGSETTINGS_RANKLEVEL
DESCRIPTOR.message_types_by_name['CombatRankingSettings'] = _COMBATRANKINGSETTINGS

CombatRankingSettings = _reflection.GeneratedProtocolMessageType('CombatRankingSettings', (_message.Message,), dict(

  RankLevel = _reflection.GeneratedProtocolMessageType('RankLevel', (_message.Message,), dict(
    DESCRIPTOR = _COMBATRANKINGSETTINGS_RANKLEVEL,
    __module__ = 'pogoprotos.settings.master.combat_ranking_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatRankingSettings.RankLevel)
    ))
  ,
  DESCRIPTOR = _COMBATRANKINGSETTINGS,
  __module__ = 'pogoprotos.settings.master.combat_ranking_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.CombatRankingSettings)
  ))
_sym_db.RegisterMessage(CombatRankingSettings)
_sym_db.RegisterMessage(CombatRankingSettings.RankLevel)


# @@protoc_insertion_point(module_scope)
