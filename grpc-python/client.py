import logging
import asyncio
import grpc

from autocode.helloworld_pb2_grpc import GreeterStub
from autocode.helloworld_pb2 import HelloRequest


async def main() -> None:

    async with grpc.aio.insecure_channel('localhost:50051') as channel:

        greeter_stub = GreeterStub(channel)

        # iterates 10 times
        for i in range(10):

            # send request and wait for response
            response = await greeter_stub.SayHello(HelloRequest(name='Fabito'))

            # print the received message
            logging.info(f'Received: {response.message}')

            # delay
            await asyncio.sleep(0.5)

    logging.info('Execution finished!')


if __name__ == '__main__':

    # configures the logger
    logging.basicConfig(level=logging.INFO)

    # executes the main application
    asyncio.run(main())
