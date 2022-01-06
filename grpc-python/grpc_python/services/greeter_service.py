import logging
import time

from grpc_python.grpc_auto.greeter_pb2_grpc import GreeterServicer
from grpc_python.grpc_auto.greeter_pb2 import HelloReply, CounterStreamReply, NamesReply


class Greeter(GreeterServicer):

    def SayHello(self, request, context):
        logging.debug(f'SayHello received: {request.name}')
        return HelloReply(message=f'Hello, {request.name}!')

    def CounterStream(self, request, context):
        counter = 0
        while True:
            logging.debug(f'CounterStream generated: {counter}')
            yield CounterStreamReply(counter=counter)
            counter += 1
            time.sleep(1)

    def GetNames(self, request, context):
        logging.debug(f'GetNames called')
        names = ["Fabio", "Elaine", "Eugenio"]
        return NamesReply(names=names)
