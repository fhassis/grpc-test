# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Candles.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Candles.proto',
  package='metatrader',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rCandles.proto\x12\nmetatrader\"^\n\x06\x43\x61ndle\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0c\n\x04open\x18\x02 \x01(\x02\x12\x0c\n\x04high\x18\x03 \x01(\x02\x12\x0b\n\x03low\x18\x04 \x01(\x02\x12\r\n\x05\x63lose\x18\x05 \x01(\x02\x12\x0e\n\x06volume\x18\x06 \x01(\x02\"]\n\x11GetLastCandlesReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12(\n\ttimeframe\x18\x02 \x01(\x0e\x32\x15.metatrader.Timeframe\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"]\n\x12GetCandlesSinceReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12(\n\ttimeframe\x18\x02 \x01(\x0e\x32\x15.metatrader.Timeframe\x12\r\n\x05since\x18\x03 \x01(\x03\"1\n\nCandleList\x12#\n\x07\x63\x61ndles\x18\x01 \x03(\x0b\x32\x12.metatrader.Candle*4\n\tTimeframe\x12\x06\n\x02M1\x10\x00\x12\x07\n\x03M15\x10\x01\x12\x06\n\x02H1\x10\x02\x12\x06\n\x02H4\x10\x03\x12\x06\n\x02\x44\x31\x10\x04\x32\xa3\x01\n\rCandleService\x12G\n\x0eGetLastCandles\x12\x1d.metatrader.GetLastCandlesReq\x1a\x16.metatrader.CandleList\x12I\n\x0fGetCandlesSince\x12\x1e.metatrader.GetCandlesSinceReq\x1a\x16.metatrader.CandleListb\x06proto3'
)

_TIMEFRAME = _descriptor.EnumDescriptor(
  name='Timeframe',
  full_name='metatrader.Timeframe',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='M1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M15', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='H1', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='H4', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='D1', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=366,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_TIMEFRAME)

Timeframe = enum_type_wrapper.EnumTypeWrapper(_TIMEFRAME)
M1 = 0
M15 = 1
H1 = 2
H4 = 3
D1 = 4



_CANDLE = _descriptor.Descriptor(
  name='Candle',
  full_name='metatrader.Candle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='metatrader.Candle.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open', full_name='metatrader.Candle.open', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high', full_name='metatrader.Candle.high', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low', full_name='metatrader.Candle.low', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close', full_name='metatrader.Candle.close', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='metatrader.Candle.volume', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=29,
  serialized_end=123,
)


_GETLASTCANDLESREQ = _descriptor.Descriptor(
  name='GetLastCandlesReq',
  full_name='metatrader.GetLastCandlesReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='metatrader.GetLastCandlesReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeframe', full_name='metatrader.GetLastCandlesReq.timeframe', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='metatrader.GetLastCandlesReq.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=125,
  serialized_end=218,
)


_GETCANDLESSINCEREQ = _descriptor.Descriptor(
  name='GetCandlesSinceReq',
  full_name='metatrader.GetCandlesSinceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='metatrader.GetCandlesSinceReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeframe', full_name='metatrader.GetCandlesSinceReq.timeframe', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='since', full_name='metatrader.GetCandlesSinceReq.since', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=220,
  serialized_end=313,
)


_CANDLELIST = _descriptor.Descriptor(
  name='CandleList',
  full_name='metatrader.CandleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='candles', full_name='metatrader.CandleList.candles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=315,
  serialized_end=364,
)

_GETLASTCANDLESREQ.fields_by_name['timeframe'].enum_type = _TIMEFRAME
_GETCANDLESSINCEREQ.fields_by_name['timeframe'].enum_type = _TIMEFRAME
_CANDLELIST.fields_by_name['candles'].message_type = _CANDLE
DESCRIPTOR.message_types_by_name['Candle'] = _CANDLE
DESCRIPTOR.message_types_by_name['GetLastCandlesReq'] = _GETLASTCANDLESREQ
DESCRIPTOR.message_types_by_name['GetCandlesSinceReq'] = _GETCANDLESSINCEREQ
DESCRIPTOR.message_types_by_name['CandleList'] = _CANDLELIST
DESCRIPTOR.enum_types_by_name['Timeframe'] = _TIMEFRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Candle = _reflection.GeneratedProtocolMessageType('Candle', (_message.Message,), {
  'DESCRIPTOR' : _CANDLE,
  '__module__' : 'Candles_pb2'
  # @@protoc_insertion_point(class_scope:metatrader.Candle)
  })
_sym_db.RegisterMessage(Candle)

GetLastCandlesReq = _reflection.GeneratedProtocolMessageType('GetLastCandlesReq', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTCANDLESREQ,
  '__module__' : 'Candles_pb2'
  # @@protoc_insertion_point(class_scope:metatrader.GetLastCandlesReq)
  })
_sym_db.RegisterMessage(GetLastCandlesReq)

GetCandlesSinceReq = _reflection.GeneratedProtocolMessageType('GetCandlesSinceReq', (_message.Message,), {
  'DESCRIPTOR' : _GETCANDLESSINCEREQ,
  '__module__' : 'Candles_pb2'
  # @@protoc_insertion_point(class_scope:metatrader.GetCandlesSinceReq)
  })
_sym_db.RegisterMessage(GetCandlesSinceReq)

CandleList = _reflection.GeneratedProtocolMessageType('CandleList', (_message.Message,), {
  'DESCRIPTOR' : _CANDLELIST,
  '__module__' : 'Candles_pb2'
  # @@protoc_insertion_point(class_scope:metatrader.CandleList)
  })
_sym_db.RegisterMessage(CandleList)



_CANDLESERVICE = _descriptor.ServiceDescriptor(
  name='CandleService',
  full_name='metatrader.CandleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=421,
  serialized_end=584,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLastCandles',
    full_name='metatrader.CandleService.GetLastCandles',
    index=0,
    containing_service=None,
    input_type=_GETLASTCANDLESREQ,
    output_type=_CANDLELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCandlesSince',
    full_name='metatrader.CandleService.GetCandlesSince',
    index=1,
    containing_service=None,
    input_type=_GETCANDLESSINCEREQ,
    output_type=_CANDLELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CANDLESERVICE)

DESCRIPTOR.services_by_name['CandleService'] = _CANDLESERVICE

# @@protoc_insertion_point(module_scope)
