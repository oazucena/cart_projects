# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: car.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='car.proto',
  package='omicron',
  syntax='proto3',
  serialized_options=b'\n\023io.grpc.omicron.carB\016CarServerProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tcar.proto\x12\x07omicron\"\x07\n\x05\x45mpty\"H\n\x10\x44irectionRequest\x12\r\n\x05speed\x18\x01 \x01(\x05\x12%\n\tdirection\x18\x02 \x01(\x0e\x32\x12.omicron.Direction\"/\n\x0c\x41\x63\x63\x65leration\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\";\n\x0c\x43\x61rStateInfo\x12+\n\x0c\x61\x63\x63\x65leration\x18\x01 \x01(\x0b\x32\x15.omicron.Acceleration\"j\n\x12\x43\x61rStateInfoStatus\x12\x33\n\x05state\x18\x01 \x01(\x0e\x32$.omicron.CarStateInfoStatus.CarState\"\x1f\n\x08\x43\x61rState\x12\t\n\x05START\x10\x00\x12\x08\n\x04STOP\x10\x01\"!\n\x0e\x44irectionReply\x12\x0f\n\x07message\x18\x01 \x01(\t*E\n\tDirection\x12\x0b\n\x07\x46ORWARD\x10\x00\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x03\x12\x08\n\x04STOP\x10\x04\x32\xb7\x01\n\x03\x43\x61r\x12\x41\n\tdirection\x12\x19.omicron.DirectionRequest\x1a\x17.omicron.DirectionReply\"\x00\x12\x32\n\x05state\x12\x0e.omicron.Empty\x1a\x15.omicron.CarStateInfo\"\x00\x30\x01\x12\x39\n\x06\x63hange\x12\x1b.omicron.CarStateInfoStatus\x1a\x0e.omicron.Empty\"\x00(\x01\x42-\n\x13io.grpc.omicron.carB\x0e\x43\x61rServerProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='omicron.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORWARD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BACKWARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=358,
  serialized_end=427,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT = 3
STOP = 4


_CARSTATEINFOSTATUS_CARSTATE = _descriptor.EnumDescriptor(
  name='CarState',
  full_name='omicron.CarStateInfoStatus.CarState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=290,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_CARSTATEINFOSTATUS_CARSTATE)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='omicron.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=29,
)


_DIRECTIONREQUEST = _descriptor.Descriptor(
  name='DirectionRequest',
  full_name='omicron.DirectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='omicron.DirectionRequest.speed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='omicron.DirectionRequest.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=103,
)


_ACCELERATION = _descriptor.Descriptor(
  name='Acceleration',
  full_name='omicron.Acceleration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='omicron.Acceleration.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='omicron.Acceleration.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='omicron.Acceleration.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=152,
)


_CARSTATEINFO = _descriptor.Descriptor(
  name='CarStateInfo',
  full_name='omicron.CarStateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='omicron.CarStateInfo.acceleration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=213,
)


_CARSTATEINFOSTATUS = _descriptor.Descriptor(
  name='CarStateInfoStatus',
  full_name='omicron.CarStateInfoStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='omicron.CarStateInfoStatus.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CARSTATEINFOSTATUS_CARSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=321,
)


_DIRECTIONREPLY = _descriptor.Descriptor(
  name='DirectionReply',
  full_name='omicron.DirectionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='omicron.DirectionReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=356,
)

_DIRECTIONREQUEST.fields_by_name['direction'].enum_type = _DIRECTION
_CARSTATEINFO.fields_by_name['acceleration'].message_type = _ACCELERATION
_CARSTATEINFOSTATUS.fields_by_name['state'].enum_type = _CARSTATEINFOSTATUS_CARSTATE
_CARSTATEINFOSTATUS_CARSTATE.containing_type = _CARSTATEINFOSTATUS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['DirectionRequest'] = _DIRECTIONREQUEST
DESCRIPTOR.message_types_by_name['Acceleration'] = _ACCELERATION
DESCRIPTOR.message_types_by_name['CarStateInfo'] = _CARSTATEINFO
DESCRIPTOR.message_types_by_name['CarStateInfoStatus'] = _CARSTATEINFOSTATUS
DESCRIPTOR.message_types_by_name['DirectionReply'] = _DIRECTIONREPLY
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:omicron.Empty)
  })
_sym_db.RegisterMessage(Empty)

DirectionRequest = _reflection.GeneratedProtocolMessageType('DirectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTIONREQUEST,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:omicron.DirectionRequest)
  })
_sym_db.RegisterMessage(DirectionRequest)

Acceleration = _reflection.GeneratedProtocolMessageType('Acceleration', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATION,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:omicron.Acceleration)
  })
_sym_db.RegisterMessage(Acceleration)

CarStateInfo = _reflection.GeneratedProtocolMessageType('CarStateInfo', (_message.Message,), {
  'DESCRIPTOR' : _CARSTATEINFO,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:omicron.CarStateInfo)
  })
_sym_db.RegisterMessage(CarStateInfo)

CarStateInfoStatus = _reflection.GeneratedProtocolMessageType('CarStateInfoStatus', (_message.Message,), {
  'DESCRIPTOR' : _CARSTATEINFOSTATUS,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:omicron.CarStateInfoStatus)
  })
_sym_db.RegisterMessage(CarStateInfoStatus)

DirectionReply = _reflection.GeneratedProtocolMessageType('DirectionReply', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTIONREPLY,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:omicron.DirectionReply)
  })
_sym_db.RegisterMessage(DirectionReply)


DESCRIPTOR._options = None

_CAR = _descriptor.ServiceDescriptor(
  name='Car',
  full_name='omicron.Car',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=430,
  serialized_end=613,
  methods=[
  _descriptor.MethodDescriptor(
    name='direction',
    full_name='omicron.Car.direction',
    index=0,
    containing_service=None,
    input_type=_DIRECTIONREQUEST,
    output_type=_DIRECTIONREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='state',
    full_name='omicron.Car.state',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CARSTATEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='change',
    full_name='omicron.Car.change',
    index=2,
    containing_service=None,
    input_type=_CARSTATEINFOSTATUS,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAR)

DESCRIPTOR.services_by_name['Car'] = _CAR

# @@protoc_insertion_point(module_scope)