///
//  Generated code. Do not modify.
//  source: greeter.proto
//
// @dart = 2.12
// ignore_for_file: annotate_overrides,camel_case_types,unnecessary_const,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name,return_of_invalid_type,unnecessary_this,prefer_final_fields

import 'dart:async' as $async;

import 'dart:core' as $core;

import 'package:grpc/service_api.dart' as $grpc;
import 'greeter.pb.dart' as $0;
export 'greeter.pb.dart';

class GreeterClient extends $grpc.Client {
  static final _$sayHello = $grpc.ClientMethod<$0.HelloRequest, $0.HelloReply>(
      '/Greeter/SayHello',
      ($0.HelloRequest value) => value.writeToBuffer(),
      ($core.List<$core.int> value) => $0.HelloReply.fromBuffer(value));
  static final _$counterStream =
      $grpc.ClientMethod<$0.Empty, $0.CounterStreamReply>(
          '/Greeter/CounterStream',
          ($0.Empty value) => value.writeToBuffer(),
          ($core.List<$core.int> value) =>
              $0.CounterStreamReply.fromBuffer(value));
  static final _$getNames = $grpc.ClientMethod<$0.Empty, $0.NamesReply>(
      '/Greeter/GetNames',
      ($0.Empty value) => value.writeToBuffer(),
      ($core.List<$core.int> value) => $0.NamesReply.fromBuffer(value));

  GreeterClient($grpc.ClientChannel channel,
      {$grpc.CallOptions? options,
      $core.Iterable<$grpc.ClientInterceptor>? interceptors})
      : super(channel, options: options, interceptors: interceptors);

  $grpc.ResponseFuture<$0.HelloReply> sayHello($0.HelloRequest request,
      {$grpc.CallOptions? options}) {
    return $createUnaryCall(_$sayHello, request, options: options);
  }

  $grpc.ResponseStream<$0.CounterStreamReply> counterStream($0.Empty request,
      {$grpc.CallOptions? options}) {
    return $createStreamingCall(
        _$counterStream, $async.Stream.fromIterable([request]),
        options: options);
  }

  $grpc.ResponseFuture<$0.NamesReply> getNames($0.Empty request,
      {$grpc.CallOptions? options}) {
    return $createUnaryCall(_$getNames, request, options: options);
  }
}

abstract class GreeterServiceBase extends $grpc.Service {
  $core.String get $name => 'Greeter';

  GreeterServiceBase() {
    $addMethod($grpc.ServiceMethod<$0.HelloRequest, $0.HelloReply>(
        'SayHello',
        sayHello_Pre,
        false,
        false,
        ($core.List<$core.int> value) => $0.HelloRequest.fromBuffer(value),
        ($0.HelloReply value) => value.writeToBuffer()));
    $addMethod($grpc.ServiceMethod<$0.Empty, $0.CounterStreamReply>(
        'CounterStream',
        counterStream_Pre,
        false,
        true,
        ($core.List<$core.int> value) => $0.Empty.fromBuffer(value),
        ($0.CounterStreamReply value) => value.writeToBuffer()));
    $addMethod($grpc.ServiceMethod<$0.Empty, $0.NamesReply>(
        'GetNames',
        getNames_Pre,
        false,
        false,
        ($core.List<$core.int> value) => $0.Empty.fromBuffer(value),
        ($0.NamesReply value) => value.writeToBuffer()));
  }

  $async.Future<$0.HelloReply> sayHello_Pre(
      $grpc.ServiceCall call, $async.Future<$0.HelloRequest> request) async {
    return sayHello(call, await request);
  }

  $async.Stream<$0.CounterStreamReply> counterStream_Pre(
      $grpc.ServiceCall call, $async.Future<$0.Empty> request) async* {
    yield* counterStream(call, await request);
  }

  $async.Future<$0.NamesReply> getNames_Pre(
      $grpc.ServiceCall call, $async.Future<$0.Empty> request) async {
    return getNames(call, await request);
  }

  $async.Future<$0.HelloReply> sayHello(
      $grpc.ServiceCall call, $0.HelloRequest request);
  $async.Stream<$0.CounterStreamReply> counterStream(
      $grpc.ServiceCall call, $0.Empty request);
  $async.Future<$0.NamesReply> getNames(
      $grpc.ServiceCall call, $0.Empty request);
}
