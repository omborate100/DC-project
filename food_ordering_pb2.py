# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: food_ordering.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66ood_ordering.proto\x12\x0c\x66oodordering\"3\n\x08MenuItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\"\x10\n\x0eGetMenuRequest\"5\n\x0cMenuResponse\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.foodordering.MenuItem\"%\n\x11PlaceOrderRequest\x12\x10\n\x08item_ids\x18\x01 \x03(\t\"6\n\rOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x13\n\x0btotal_price\x18\x02 \x01(\x02\"\x13\n\x11ListOrdersRequest\"U\n\x05Order\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12%\n\x05items\x18\x02 \x03(\x0b\x32\x16.foodordering.MenuItem\x12\x13\n\x0btotal_price\x18\x03 \x01(\x02\"9\n\x12ListOrdersResponse\x12#\n\x06orders\x18\x01 \x03(\x0b\x32\x13.foodordering.Order2\xf6\x01\n\x0c\x46oodOrdering\x12\x45\n\x07GetMenu\x12\x1c.foodordering.GetMenuRequest\x1a\x1a.foodordering.MenuResponse\"\x00\x12L\n\nPlaceOrder\x12\x1f.foodordering.PlaceOrderRequest\x1a\x1b.foodordering.OrderResponse\"\x00\x12Q\n\nListOrders\x12\x1f.foodordering.ListOrdersRequest\x1a .foodordering.ListOrdersResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'food_ordering_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MENUITEM']._serialized_start=37
  _globals['_MENUITEM']._serialized_end=88
  _globals['_GETMENUREQUEST']._serialized_start=90
  _globals['_GETMENUREQUEST']._serialized_end=106
  _globals['_MENURESPONSE']._serialized_start=108
  _globals['_MENURESPONSE']._serialized_end=161
  _globals['_PLACEORDERREQUEST']._serialized_start=163
  _globals['_PLACEORDERREQUEST']._serialized_end=200
  _globals['_ORDERRESPONSE']._serialized_start=202
  _globals['_ORDERRESPONSE']._serialized_end=256
  _globals['_LISTORDERSREQUEST']._serialized_start=258
  _globals['_LISTORDERSREQUEST']._serialized_end=277
  _globals['_ORDER']._serialized_start=279
  _globals['_ORDER']._serialized_end=364
  _globals['_LISTORDERSRESPONSE']._serialized_start=366
  _globals['_LISTORDERSRESPONSE']._serialized_end=423
  _globals['_FOODORDERING']._serialized_start=426
  _globals['_FOODORDERING']._serialized_end=672
# @@protoc_insertion_point(module_scope)
