import 'package:grpc/grpc.dart';

import '../../protocol_buffers/dart/greeter.pbgrpc.dart';

class GreeterService extends GreeterServiceBase {
  @override
  Future<HelloReply> sayHello(ServiceCall call, HelloRequest request) async {
    return HelloReply(message: "Hello, ${request.name}!");
  }

  @override
  Stream<CounterStreamReply> counterStream(ServiceCall call, Empty request) async* {
    int counter = 0;
    while (true) {
      yield CounterStreamReply(counter: counter);
      counter++;
      await Future.delayed(Duration(seconds: 1));
    }
  }

  @override
  Future<NamesReply> getNames(ServiceCall call, Empty request) async {
    const names = ['John', 'Mary', 'Peter'];
    return NamesReply(names: names);
  }
}

void main() async {
  var server = Server([GreeterService()]);
  await server.serve(port: 8080);
  print('Dart server listening on port ${server.port}...');
}
