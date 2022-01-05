import logging
from autocode.helloworld_pb2_grpc import GreeterServicer
from autocode.helloworld_pb2 import HelloReply


class Greeter(GreeterServicer):

    def SayHello(self, request, context):
        logging.debug(f'Received {request.name}')
        return HelloReply(message=f'Hello, {request.name}!')

    def SayHelloAgain(self, request, context):
        logging.debug(f'Received {request.name}')
        return HelloReply(message=f'Hello again, {request.name}')
