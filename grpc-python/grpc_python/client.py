import logging
from asyncio import sleep, run
from grpc.aio import insecure_channel

# adding autocode folder due to limitations in code generation
import sys
sys.path.append("autocode")

from autocode.greeter_pb2_grpc import GreeterStub
from autocode.greeter_pb2 import HelloRequest


async def main(host: str, port: int) -> None:

    async with insecure_channel(f"{host}:{port}") as channel:

        greeter_stub = GreeterStub(channel)

        # iterates 10 times
        for i in range(10):

            # send request and wait for response
            response = await greeter_stub.SayHello(HelloRequest(name="Fabito"))

            # print the received message
            logging.info(f"Received: {response.message}")

            # delay
            await sleep(0.5)

    logging.info("Execution finished!")


if __name__ == "__main__":

    # configures the logger
    logging.basicConfig(level=logging.INFO)

    # executes the main application
    run(main("localhost", 9090))
