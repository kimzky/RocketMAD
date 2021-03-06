# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import quest_type_pb2 as pogoprotos_dot_enums_dot_quest__type__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.data.quests import catch_pokemon_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_catch__pokemon__quest__pb2
from pogoprotos.data.quests import quest_reward_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2
from pogoprotos.data.quests import quest_goal_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__goal__pb2
from pogoprotos.data.quests import add_friend_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_add__friend__quest__pb2
from pogoprotos.data.quests import trade_pokemon_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_trade__pokemon__quest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_pb=_b('\n\"pogoprotos/data/quests/quest.proto\x12\x16pogoprotos.data.quests\x1a!pogoprotos/enums/quest_type.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a\x30pogoprotos/data/quests/catch_pokemon_quest.proto\x1a)pogoprotos/data/quests/quest_reward.proto\x1a\'pogoprotos/data/quests/quest_goal.proto\x1a-pogoprotos/data/quests/add_friend_quest.proto\x1a\x30pogoprotos/data/quests/trade_pokemon_quest.proto\"\xaa\x10\n\x05Quest\x12/\n\nquest_type\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.QuestType\x12?\n\x0b\x64\x61ily_quest\x18\x02 \x01(\x0b\x32(.pogoprotos.data.quests.Quest.DailyQuestH\x00\x12\x42\n\nmulti_part\x18\x03 \x01(\x0b\x32,.pogoprotos.data.quests.Quest.MultiPartQuestH\x00\x12\x42\n\rcatch_pokemon\x18\x04 \x01(\x0b\x32).pogoprotos.data.quests.CatchPokemonQuestH\x00\x12<\n\nadd_friend\x18\x05 \x01(\x0b\x32&.pogoprotos.data.quests.AddFriendQuestH\x00\x12\x42\n\rtrade_pokemon\x18\x06 \x01(\x0b\x32).pogoprotos.data.quests.TradePokemonQuestH\x00\x12W\n\x15\x64\x61ily_buddy_affection\x18\x07 \x01(\x0b\x32\x36.pogoprotos.data.quests.Quest.DailyBuddyAffectionQuestH\x00\x12=\n\nquest_walk\x18\x08 \x01(\x0b\x32\'.pogoprotos.data.quests.Quest.QuestWalkH\x00\x12S\n\x13\x65volve_into_pokemon\x18\t \x01(\x0b\x32\x34.pogoprotos.data.quests.Quest.EvolveIntoPokemonQuestH\x00\x12\x45\n\x0c\x64\x61ys_in_arow\x18\x63 \x01(\x0b\x32/.pogoprotos.data.quests.Quest.DaysWithARowQuest\x12\x10\n\x08quest_id\x18\x64 \x01(\t\x12\x12\n\nquest_seed\x18\x65 \x01(\x03\x12<\n\rquest_context\x18\x66 \x01(\x0e\x32%.pogoprotos.data.quests.Quest.Context\x12\x13\n\x0btemplate_id\x18g \x01(\t\x12\x10\n\x08progress\x18h \x01(\x05\x12/\n\x04goal\x18i \x01(\x0b\x32!.pogoprotos.data.quests.QuestGoal\x12\x34\n\x06status\x18j \x01(\x0e\x32$.pogoprotos.data.quests.Quest.Status\x12:\n\rquest_rewards\x18k \x03(\x0b\x32#.pogoprotos.data.quests.QuestReward\x12\x1d\n\x15\x63reation_timestamp_ms\x18l \x01(\x03\x12 \n\x18last_update_timestamp_ms\x18m \x01(\x03\x12 \n\x18\x63ompeletion_timestamp_ms\x18n \x01(\x03\x12\x0f\n\x07\x66ort_id\x18o \x01(\t\x12\x17\n\x0f\x61\x64min_generated\x18p \x01(\x08\x12$\n\x1cstamp_count_override_enabled\x18q \x01(\x08\x12\x1c\n\x14stamp_count_override\x18r \x01(\x05\x12\x12\n\ns2_cell_id\x18s \x01(\x03\x12$\n\x1cstory_quest_template_version\x18t \x01(\x05\x12\x41\n\rdaily_counter\x18u \x01(\x0b\x32*.pogoprotos.data.quests.Quest.DailyCounter\x12\x1f\n\x17reward_pokemon_icon_url\x18v \x01(\t\x12\x18\n\x10\x65nd_timestamp_ms\x18w \x01(\x03\x1a*\n\tQuestWalk\x12\x1d\n\x15quest_start_km_walked\x18\x01 \x01(\x02\x1aP\n\x16\x45volveIntoPokemonQuest\x12\x36\n\x11unique_pokemon_id\x18\x01 \x03(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x1a(\n\x11\x44\x61ysWithARowQuest\x12\x13\n\x0blast_window\x18\x01 \x01(\x05\x1ag\n\x18\x44\x61ilyBuddyAffectionQuest\x12K\n\x17\x64\x61ily_affection_counter\x18\x01 \x01(\x0b\x32*.pogoprotos.data.quests.Quest.DailyCounter\x1a\x43\n\x0eMultiPartQuest\x12\x31\n\nsub_quests\x18\x01 \x03(\x0b\x32\x1d.pogoprotos.data.quests.Quest\x1aI\n\nDailyQuest\x12\x1d\n\x15\x63urrent_period_bucket\x18\x01 \x01(\x05\x12\x1c\n\x14\x63urrent_streak_count\x18\x02 \x01(\x05\x1a\x46\n\x0c\x44\x61ilyCounter\x12\x0e\n\x06window\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x17\n\x0f\x62uckets_per_day\x18\x03 \x01(\x05\"\x7f\n\x07\x43ontext\x12\t\n\x05UNSET\x10\x00\x12\x0f\n\x0bSTORY_QUEST\x10\x01\x12\x13\n\x0f\x43HALLENGE_QUEST\x10\x02\x12\x14\n\x10\x44\x41ILY_COIN_QUEST\x10\x03\x12\x15\n\x11TIMED_STORY_QUEST\x10\x04\x12\x16\n\x12TGC_TRACKING_QUEST\x10\x07\"G\n\x06Status\x12\x14\n\x10STATUS_UNDEFINED\x10\x00\x12\x11\n\rSTATUS_ACTIVE\x10\x01\x12\x14\n\x10STATUS_COMPLETED\x10\x02\x42\x07\n\x05Questb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_quest__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_catch__pokemon__quest__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__goal__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_add__friend__quest__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_trade__pokemon__quest__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_QUEST_CONTEXT = _descriptor.EnumDescriptor(
  name='Context',
  full_name='pogoprotos.data.quests.Quest.Context',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORY_QUEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_QUEST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAILY_COIN_QUEST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_STORY_QUEST', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TGC_TRACKING_QUEST', index=5, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2245,
  serialized_end=2372,
)
_sym_db.RegisterEnumDescriptor(_QUEST_CONTEXT)

_QUEST_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.data.quests.Quest.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_COMPLETED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2374,
  serialized_end=2445,
)
_sym_db.RegisterEnumDescriptor(_QUEST_STATUS)


_QUEST_QUESTWALK = _descriptor.Descriptor(
  name='QuestWalk',
  full_name='pogoprotos.data.quests.Quest.QuestWalk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_start_km_walked', full_name='pogoprotos.data.quests.Quest.QuestWalk.quest_start_km_walked', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1756,
  serialized_end=1798,
)

_QUEST_EVOLVEINTOPOKEMONQUEST = _descriptor.Descriptor(
  name='EvolveIntoPokemonQuest',
  full_name='pogoprotos.data.quests.Quest.EvolveIntoPokemonQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unique_pokemon_id', full_name='pogoprotos.data.quests.Quest.EvolveIntoPokemonQuest.unique_pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=3,
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
  serialized_start=1800,
  serialized_end=1880,
)

_QUEST_DAYSWITHAROWQUEST = _descriptor.Descriptor(
  name='DaysWithARowQuest',
  full_name='pogoprotos.data.quests.Quest.DaysWithARowQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_window', full_name='pogoprotos.data.quests.Quest.DaysWithARowQuest.last_window', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1882,
  serialized_end=1922,
)

_QUEST_DAILYBUDDYAFFECTIONQUEST = _descriptor.Descriptor(
  name='DailyBuddyAffectionQuest',
  full_name='pogoprotos.data.quests.Quest.DailyBuddyAffectionQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_affection_counter', full_name='pogoprotos.data.quests.Quest.DailyBuddyAffectionQuest.daily_affection_counter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1924,
  serialized_end=2027,
)

_QUEST_MULTIPARTQUEST = _descriptor.Descriptor(
  name='MultiPartQuest',
  full_name='pogoprotos.data.quests.Quest.MultiPartQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub_quests', full_name='pogoprotos.data.quests.Quest.MultiPartQuest.sub_quests', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=2029,
  serialized_end=2096,
)

_QUEST_DAILYQUEST = _descriptor.Descriptor(
  name='DailyQuest',
  full_name='pogoprotos.data.quests.Quest.DailyQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_period_bucket', full_name='pogoprotos.data.quests.Quest.DailyQuest.current_period_bucket', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_streak_count', full_name='pogoprotos.data.quests.Quest.DailyQuest.current_streak_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=2098,
  serialized_end=2171,
)

_QUEST_DAILYCOUNTER = _descriptor.Descriptor(
  name='DailyCounter',
  full_name='pogoprotos.data.quests.Quest.DailyCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window', full_name='pogoprotos.data.quests.Quest.DailyCounter.window', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='pogoprotos.data.quests.Quest.DailyCounter.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buckets_per_day', full_name='pogoprotos.data.quests.Quest.DailyCounter.buckets_per_day', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=2173,
  serialized_end=2243,
)

_QUEST = _descriptor.Descriptor(
  name='Quest',
  full_name='pogoprotos.data.quests.Quest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_type', full_name='pogoprotos.data.quests.Quest.quest_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_quest', full_name='pogoprotos.data.quests.Quest.daily_quest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_part', full_name='pogoprotos.data.quests.Quest.multi_part', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='catch_pokemon', full_name='pogoprotos.data.quests.Quest.catch_pokemon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_friend', full_name='pogoprotos.data.quests.Quest.add_friend', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trade_pokemon', full_name='pogoprotos.data.quests.Quest.trade_pokemon', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_buddy_affection', full_name='pogoprotos.data.quests.Quest.daily_buddy_affection', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_walk', full_name='pogoprotos.data.quests.Quest.quest_walk', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolve_into_pokemon', full_name='pogoprotos.data.quests.Quest.evolve_into_pokemon', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days_in_arow', full_name='pogoprotos.data.quests.Quest.days_in_arow', index=9,
      number=99, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_id', full_name='pogoprotos.data.quests.Quest.quest_id', index=10,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_seed', full_name='pogoprotos.data.quests.Quest.quest_seed', index=11,
      number=101, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_context', full_name='pogoprotos.data.quests.Quest.quest_context', index=12,
      number=102, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='pogoprotos.data.quests.Quest.template_id', index=13,
      number=103, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='pogoprotos.data.quests.Quest.progress', index=14,
      number=104, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goal', full_name='pogoprotos.data.quests.Quest.goal', index=15,
      number=105, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.data.quests.Quest.status', index=16,
      number=106, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_rewards', full_name='pogoprotos.data.quests.Quest.quest_rewards', index=17,
      number=107, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_timestamp_ms', full_name='pogoprotos.data.quests.Quest.creation_timestamp_ms', index=18,
      number=108, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_update_timestamp_ms', full_name='pogoprotos.data.quests.Quest.last_update_timestamp_ms', index=19,
      number=109, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compeletion_timestamp_ms', full_name='pogoprotos.data.quests.Quest.compeletion_timestamp_ms', index=20,
      number=110, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.data.quests.Quest.fort_id', index=21,
      number=111, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='admin_generated', full_name='pogoprotos.data.quests.Quest.admin_generated', index=22,
      number=112, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamp_count_override_enabled', full_name='pogoprotos.data.quests.Quest.stamp_count_override_enabled', index=23,
      number=113, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamp_count_override', full_name='pogoprotos.data.quests.Quest.stamp_count_override', index=24,
      number=114, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s2_cell_id', full_name='pogoprotos.data.quests.Quest.s2_cell_id', index=25,
      number=115, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='story_quest_template_version', full_name='pogoprotos.data.quests.Quest.story_quest_template_version', index=26,
      number=116, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_counter', full_name='pogoprotos.data.quests.Quest.daily_counter', index=27,
      number=117, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_pokemon_icon_url', full_name='pogoprotos.data.quests.Quest.reward_pokemon_icon_url', index=28,
      number=118, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp_ms', full_name='pogoprotos.data.quests.Quest.end_timestamp_ms', index=29,
      number=119, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_QUEST_QUESTWALK, _QUEST_EVOLVEINTOPOKEMONQUEST, _QUEST_DAYSWITHAROWQUEST, _QUEST_DAILYBUDDYAFFECTIONQUEST, _QUEST_MULTIPARTQUEST, _QUEST_DAILYQUEST, _QUEST_DAILYCOUNTER, ],
  enum_types=[
    _QUEST_CONTEXT,
    _QUEST_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Quest', full_name='pogoprotos.data.quests.Quest.Quest',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=364,
  serialized_end=2454,
)

_QUEST_QUESTWALK.containing_type = _QUEST
_QUEST_EVOLVEINTOPOKEMONQUEST.fields_by_name['unique_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_QUEST_EVOLVEINTOPOKEMONQUEST.containing_type = _QUEST
_QUEST_DAYSWITHAROWQUEST.containing_type = _QUEST
_QUEST_DAILYBUDDYAFFECTIONQUEST.fields_by_name['daily_affection_counter'].message_type = _QUEST_DAILYCOUNTER
_QUEST_DAILYBUDDYAFFECTIONQUEST.containing_type = _QUEST
_QUEST_MULTIPARTQUEST.fields_by_name['sub_quests'].message_type = _QUEST
_QUEST_MULTIPARTQUEST.containing_type = _QUEST
_QUEST_DAILYQUEST.containing_type = _QUEST
_QUEST_DAILYCOUNTER.containing_type = _QUEST
_QUEST.fields_by_name['quest_type'].enum_type = pogoprotos_dot_enums_dot_quest__type__pb2._QUESTTYPE
_QUEST.fields_by_name['daily_quest'].message_type = _QUEST_DAILYQUEST
_QUEST.fields_by_name['multi_part'].message_type = _QUEST_MULTIPARTQUEST
_QUEST.fields_by_name['catch_pokemon'].message_type = pogoprotos_dot_data_dot_quests_dot_catch__pokemon__quest__pb2._CATCHPOKEMONQUEST
_QUEST.fields_by_name['add_friend'].message_type = pogoprotos_dot_data_dot_quests_dot_add__friend__quest__pb2._ADDFRIENDQUEST
_QUEST.fields_by_name['trade_pokemon'].message_type = pogoprotos_dot_data_dot_quests_dot_trade__pokemon__quest__pb2._TRADEPOKEMONQUEST
_QUEST.fields_by_name['daily_buddy_affection'].message_type = _QUEST_DAILYBUDDYAFFECTIONQUEST
_QUEST.fields_by_name['quest_walk'].message_type = _QUEST_QUESTWALK
_QUEST.fields_by_name['evolve_into_pokemon'].message_type = _QUEST_EVOLVEINTOPOKEMONQUEST
_QUEST.fields_by_name['days_in_arow'].message_type = _QUEST_DAYSWITHAROWQUEST
_QUEST.fields_by_name['quest_context'].enum_type = _QUEST_CONTEXT
_QUEST.fields_by_name['goal'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__goal__pb2._QUESTGOAL
_QUEST.fields_by_name['status'].enum_type = _QUEST_STATUS
_QUEST.fields_by_name['quest_rewards'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2._QUESTREWARD
_QUEST.fields_by_name['daily_counter'].message_type = _QUEST_DAILYCOUNTER
_QUEST_CONTEXT.containing_type = _QUEST
_QUEST_STATUS.containing_type = _QUEST
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['daily_quest'])
_QUEST.fields_by_name['daily_quest'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['multi_part'])
_QUEST.fields_by_name['multi_part'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['catch_pokemon'])
_QUEST.fields_by_name['catch_pokemon'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['add_friend'])
_QUEST.fields_by_name['add_friend'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['trade_pokemon'])
_QUEST.fields_by_name['trade_pokemon'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['daily_buddy_affection'])
_QUEST.fields_by_name['daily_buddy_affection'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['quest_walk'])
_QUEST.fields_by_name['quest_walk'].containing_oneof = _QUEST.oneofs_by_name['Quest']
_QUEST.oneofs_by_name['Quest'].fields.append(
  _QUEST.fields_by_name['evolve_into_pokemon'])
_QUEST.fields_by_name['evolve_into_pokemon'].containing_oneof = _QUEST.oneofs_by_name['Quest']
DESCRIPTOR.message_types_by_name['Quest'] = _QUEST

Quest = _reflection.GeneratedProtocolMessageType('Quest', (_message.Message,), dict(

  QuestWalk = _reflection.GeneratedProtocolMessageType('QuestWalk', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_QUESTWALK,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.QuestWalk)
    ))
  ,

  EvolveIntoPokemonQuest = _reflection.GeneratedProtocolMessageType('EvolveIntoPokemonQuest', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_EVOLVEINTOPOKEMONQUEST,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.EvolveIntoPokemonQuest)
    ))
  ,

  DaysWithARowQuest = _reflection.GeneratedProtocolMessageType('DaysWithARowQuest', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_DAYSWITHAROWQUEST,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.DaysWithARowQuest)
    ))
  ,

  DailyBuddyAffectionQuest = _reflection.GeneratedProtocolMessageType('DailyBuddyAffectionQuest', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_DAILYBUDDYAFFECTIONQUEST,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.DailyBuddyAffectionQuest)
    ))
  ,

  MultiPartQuest = _reflection.GeneratedProtocolMessageType('MultiPartQuest', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_MULTIPARTQUEST,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.MultiPartQuest)
    ))
  ,

  DailyQuest = _reflection.GeneratedProtocolMessageType('DailyQuest', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_DAILYQUEST,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.DailyQuest)
    ))
  ,

  DailyCounter = _reflection.GeneratedProtocolMessageType('DailyCounter', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_DAILYCOUNTER,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.DailyCounter)
    ))
  ,
  DESCRIPTOR = _QUEST,
  __module__ = 'pogoprotos.data.quests.quest_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest)
  ))
_sym_db.RegisterMessage(Quest)
_sym_db.RegisterMessage(Quest.QuestWalk)
_sym_db.RegisterMessage(Quest.EvolveIntoPokemonQuest)
_sym_db.RegisterMessage(Quest.DaysWithARowQuest)
_sym_db.RegisterMessage(Quest.DailyBuddyAffectionQuest)
_sym_db.RegisterMessage(Quest.MultiPartQuest)
_sym_db.RegisterMessage(Quest.DailyQuest)
_sym_db.RegisterMessage(Quest.DailyCounter)


# @@protoc_insertion_point(module_scope)
