///
//  Generated code. Do not modify.
//  source: greeter.proto
//
// @dart = 2.12
// ignore_for_file: annotate_overrides,camel_case_types,unnecessary_const,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name,return_of_invalid_type,unnecessary_this,prefer_final_fields,deprecated_member_use_from_same_package

import 'dart:core' as $core;
import 'dart:convert' as $convert;
import 'dart:typed_data' as $typed_data;
@$core.Deprecated('Use helloRequestDescriptor instead')
const HelloRequest$json = const {
  '1': 'HelloRequest',
  '2': const [
    const {'1': 'name', '3': 1, '4': 1, '5': 9, '10': 'name'},
  ],
};

/// Descriptor for `HelloRequest`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List helloRequestDescriptor = $convert.base64Decode('CgxIZWxsb1JlcXVlc3QSEgoEbmFtZRgBIAEoCVIEbmFtZQ==');
@$core.Deprecated('Use helloReplyDescriptor instead')
const HelloReply$json = const {
  '1': 'HelloReply',
  '2': const [
    const {'1': 'message', '3': 1, '4': 1, '5': 9, '10': 'message'},
  ],
};

/// Descriptor for `HelloReply`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List helloReplyDescriptor = $convert.base64Decode('CgpIZWxsb1JlcGx5EhgKB21lc3NhZ2UYASABKAlSB21lc3NhZ2U=');
@$core.Deprecated('Use counterStreamReplyDescriptor instead')
const CounterStreamReply$json = const {
  '1': 'CounterStreamReply',
  '2': const [
    const {'1': 'counter', '3': 1, '4': 1, '5': 5, '10': 'counter'},
  ],
};

/// Descriptor for `CounterStreamReply`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List counterStreamReplyDescriptor = $convert.base64Decode('ChJDb3VudGVyU3RyZWFtUmVwbHkSGAoHY291bnRlchgBIAEoBVIHY291bnRlcg==');
@$core.Deprecated('Use namesReplyDescriptor instead')
const NamesReply$json = const {
  '1': 'NamesReply',
  '2': const [
    const {'1': 'name', '3': 1, '4': 3, '5': 9, '10': 'name'},
  ],
};

/// Descriptor for `NamesReply`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List namesReplyDescriptor = $convert.base64Decode('CgpOYW1lc1JlcGx5EhIKBG5hbWUYASADKAlSBG5hbWU=');
@$core.Deprecated('Use emptyDescriptor instead')
const Empty$json = const {
  '1': 'Empty',
};

/// Descriptor for `Empty`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List emptyDescriptor = $convert.base64Decode('CgVFbXB0eQ==');
