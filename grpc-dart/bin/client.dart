import 'package:grpc/grpc.dart';

import '../../protocol_buffers/dart/greeter.pbgrpc.dart';

void main() async {
  final channel = ClientChannel(
    'localhost',
    port: 8080,
    options: const ChannelOptions(credentials: ChannelCredentials.insecure()),
  );

  // create the stub to handle the greeter api
  final greeterStub = GreeterClient(channel);

  // performs some test calls
  try {
    // send a sayHello message
    final sayHelloResponse = await greeterStub.sayHello(HelloRequest(name: 'Fabio'));
    print('SayHello response: ${sayHelloResponse.message}');

    // get all names
    final getNamesResponse = await greeterStub.getNames(Empty());
    print('getNames response: ${getNamesResponse.names}');

    // subscribes to counterStream
    final counterStream = greeterStub.counterStream(Empty());
    counterStream.listen((message) {
      print('counterStream data: ${message.counter}');
    });
  } catch (e) {
    print('Caught error: $e');
  }
}
