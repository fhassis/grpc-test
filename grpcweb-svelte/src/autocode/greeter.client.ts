// @generated by protobuf-ts 2.8.2 with parameter optimize_code_size
// @generated from protobuf file "greeter.proto" (package "greeter", syntax proto3)
// tslint:disable
import type { RpcTransport } from "@protobuf-ts/runtime-rpc";
import type { ServiceInfo } from "@protobuf-ts/runtime-rpc";
import { Greeter } from "./greeter";
import type { NamesReply } from "./greeter";
import type { CounterStreamReply } from "./greeter";
import type { Empty } from "./greeter";
import type { ServerStreamingCall } from "@protobuf-ts/runtime-rpc";
import { stackIntercept } from "@protobuf-ts/runtime-rpc";
import type { HelloReply } from "./greeter";
import type { HelloRequest } from "./greeter";
import type { UnaryCall } from "@protobuf-ts/runtime-rpc";
import type { RpcOptions } from "@protobuf-ts/runtime-rpc";
/**
 * The greeting service definition.
 *
 * @generated from protobuf service greeter.Greeter
 */
export interface IGreeterClient {
    /**
     * Sends a greeting
     *
     * @generated from protobuf rpc: SayHello(greeter.HelloRequest) returns (greeter.HelloReply);
     */
    sayHello(input: HelloRequest, options?: RpcOptions): UnaryCall<HelloRequest, HelloReply>;
    /**
     * Sends a counter every second
     *
     * @generated from protobuf rpc: CounterStream(greeter.Empty) returns (stream greeter.CounterStreamReply);
     */
    counterStream(input: Empty, options?: RpcOptions): ServerStreamingCall<Empty, CounterStreamReply>;
    /**
     * Sends a list of names
     *
     * @generated from protobuf rpc: GetNames(greeter.Empty) returns (greeter.NamesReply);
     */
    getNames(input: Empty, options?: RpcOptions): UnaryCall<Empty, NamesReply>;
}
/**
 * The greeting service definition.
 *
 * @generated from protobuf service greeter.Greeter
 */
export class GreeterClient implements IGreeterClient, ServiceInfo {
    typeName = Greeter.typeName;
    methods = Greeter.methods;
    options = Greeter.options;
    constructor(private readonly _transport: RpcTransport) {
    }
    /**
     * Sends a greeting
     *
     * @generated from protobuf rpc: SayHello(greeter.HelloRequest) returns (greeter.HelloReply);
     */
    sayHello(input: HelloRequest, options?: RpcOptions): UnaryCall<HelloRequest, HelloReply> {
        const method = this.methods[0], opt = this._transport.mergeOptions(options);
        return stackIntercept<HelloRequest, HelloReply>("unary", this._transport, method, opt, input);
    }
    /**
     * Sends a counter every second
     *
     * @generated from protobuf rpc: CounterStream(greeter.Empty) returns (stream greeter.CounterStreamReply);
     */
    counterStream(input: Empty, options?: RpcOptions): ServerStreamingCall<Empty, CounterStreamReply> {
        const method = this.methods[1], opt = this._transport.mergeOptions(options);
        return stackIntercept<Empty, CounterStreamReply>("serverStreaming", this._transport, method, opt, input);
    }
    /**
     * Sends a list of names
     *
     * @generated from protobuf rpc: GetNames(greeter.Empty) returns (greeter.NamesReply);
     */
    getNames(input: Empty, options?: RpcOptions): UnaryCall<Empty, NamesReply> {
        const method = this.methods[2], opt = this._transport.mergeOptions(options);
        return stackIntercept<Empty, NamesReply>("unary", this._transport, method, opt, input);
    }
}