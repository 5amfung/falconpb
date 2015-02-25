# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FooResource.proto

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
  name='FooResource.proto',
  package='',
  serialized_pb=_b('\n\x11\x46ooResource.proto\"p\n\x0b\x46ooResource\x1a/\n\x03GET\x12\n\n\x02id\x18\x01 \x02(\t\x1a\x1c\n\x08Response\x12\x10\n\x08greeting\x18\x01 \x02(\t\x1a\x30\n\x04POST\x12\x10\n\x08greeting\x18\x01 \x02(\t\x1a\x16\n\x08Response\x12\n\n\x02id\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FOORESOURCE_GET_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='FooResource.GET.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='FooResource.GET.Response.greeting', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=83,
)

_FOORESOURCE_GET = _descriptor.Descriptor(
  name='GET',
  full_name='FooResource.GET',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='FooResource.GET.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FOORESOURCE_GET_RESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=83,
)

_FOORESOURCE_POST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='FooResource.POST.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='FooResource.POST.Response.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=133,
)

_FOORESOURCE_POST = _descriptor.Descriptor(
  name='POST',
  full_name='FooResource.POST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='FooResource.POST.greeting', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FOORESOURCE_POST_RESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=133,
)

_FOORESOURCE = _descriptor.Descriptor(
  name='FooResource',
  full_name='FooResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_FOORESOURCE_GET, _FOORESOURCE_POST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=133,
)

_FOORESOURCE_GET_RESPONSE.containing_type = _FOORESOURCE_GET
_FOORESOURCE_GET.containing_type = _FOORESOURCE
_FOORESOURCE_POST_RESPONSE.containing_type = _FOORESOURCE_POST
_FOORESOURCE_POST.containing_type = _FOORESOURCE
DESCRIPTOR.message_types_by_name['FooResource'] = _FOORESOURCE

FooResource = _reflection.GeneratedProtocolMessageType('FooResource', (_message.Message,), dict(

  GET = _reflection.GeneratedProtocolMessageType('GET', (_message.Message,), dict(

    Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
      DESCRIPTOR = _FOORESOURCE_GET_RESPONSE,
      __module__ = 'FooResource_pb2'
      # @@protoc_insertion_point(class_scope:FooResource.GET.Response)
      ))
    ,
    DESCRIPTOR = _FOORESOURCE_GET,
    __module__ = 'FooResource_pb2'
    # @@protoc_insertion_point(class_scope:FooResource.GET)
    ))
  ,

  POST = _reflection.GeneratedProtocolMessageType('POST', (_message.Message,), dict(

    Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
      DESCRIPTOR = _FOORESOURCE_POST_RESPONSE,
      __module__ = 'FooResource_pb2'
      # @@protoc_insertion_point(class_scope:FooResource.POST.Response)
      ))
    ,
    DESCRIPTOR = _FOORESOURCE_POST,
    __module__ = 'FooResource_pb2'
    # @@protoc_insertion_point(class_scope:FooResource.POST)
    ))
  ,
  DESCRIPTOR = _FOORESOURCE,
  __module__ = 'FooResource_pb2'
  # @@protoc_insertion_point(class_scope:FooResource)
  ))
_sym_db.RegisterMessage(FooResource)
_sym_db.RegisterMessage(FooResource.GET)
_sym_db.RegisterMessage(FooResource.GET.Response)
_sym_db.RegisterMessage(FooResource.POST)
_sym_db.RegisterMessage(FooResource.POST.Response)


# @@protoc_insertion_point(module_scope)