# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/raid_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.enums import raid_level_pb2 as pogoprotos_dot_enums_dot_raid__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/raid/raid_info.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_pb=_b('\n$pogoprotos/data/raid/raid_info.proto\x12\x14pogoprotos.data.raid\x1a\"pogoprotos/data/pokemon_data.proto\x1a!pogoprotos/enums/raid_level.proto\"\x86\x02\n\x08RaidInfo\x12\x11\n\traid_seed\x18\x01 \x01(\x03\x12\x15\n\rraid_spawn_ms\x18\x02 \x01(\x03\x12\x16\n\x0eraid_battle_ms\x18\x03 \x01(\x03\x12\x13\n\x0braid_end_ms\x18\x04 \x01(\x03\x12\x32\n\x0craid_pokemon\x18\x05 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12/\n\nraid_level\x18\x06 \x01(\x0e\x32\x1b.pogoprotos.enums.RaidLevel\x12\x10\n\x08\x63omplete\x18\x07 \x01(\x08\x12\x14\n\x0cis_exclusive\x18\x08 \x01(\x08\x12\x16\n\x0eis_raid_hidden\x18\t \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_raid__level__pb2.DESCRIPTOR,])




_RAIDINFO = _descriptor.Descriptor(
  name='RaidInfo',
  full_name='pogoprotos.data.raid.RaidInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raid_seed', full_name='pogoprotos.data.raid.RaidInfo.raid_seed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_spawn_ms', full_name='pogoprotos.data.raid.RaidInfo.raid_spawn_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_battle_ms', full_name='pogoprotos.data.raid.RaidInfo.raid_battle_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_end_ms', full_name='pogoprotos.data.raid.RaidInfo.raid_end_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_pokemon', full_name='pogoprotos.data.raid.RaidInfo.raid_pokemon', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_level', full_name='pogoprotos.data.raid.RaidInfo.raid_level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complete', full_name='pogoprotos.data.raid.RaidInfo.complete', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_exclusive', full_name='pogoprotos.data.raid.RaidInfo.is_exclusive', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_raid_hidden', full_name='pogoprotos.data.raid.RaidInfo.is_raid_hidden', index=8,
      number=9, type=8, cpp_type=7, label=1,
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
  serialized_start=134,
  serialized_end=396,
)

_RAIDINFO.fields_by_name['raid_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_RAIDINFO.fields_by_name['raid_level'].enum_type = pogoprotos_dot_enums_dot_raid__level__pb2._RAIDLEVEL
DESCRIPTOR.message_types_by_name['RaidInfo'] = _RAIDINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidInfo = _reflection.GeneratedProtocolMessageType('RaidInfo', (_message.Message,), dict(
  DESCRIPTOR = _RAIDINFO,
  __module__ = 'pogoprotos.data.raid.raid_info_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.RaidInfo)
  ))
_sym_db.RegisterMessage(RaidInfo)


# @@protoc_insertion_point(module_scope)
