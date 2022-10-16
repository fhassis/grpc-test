import logging
from asyncio import sleep, run
from typing import Optional
from grpc.aio import insecure_channel, secure_channel
from grpc import ssl_channel_credentials
from pathlib import Path

# adding autocode folder due to limitations in code generation
import sys

sys.path.append("autocode")

from autocode.greeter_pb2_grpc import GreeterStub
from autocode.greeter_pb2 import HelloRequest


async def main(
    host: str,
    port: int,
    cert_root_path: Optional[Path] = None,
) -> None:
    """
    Interacts to a grpc server.
    """
    address = f"{host}:{port}"

    # creates the communication channel
    if cert_root_path:
        logging.info("Using secure ssl channel")
        server_credentials = open(cert_root_path, "rb").read()
        ssl_credentials = ssl_channel_credentials(server_credentials)
        channel = secure_channel(address, ssl_credentials)
    else:
        logging.info("Using insecure channel")
        channel = insecure_channel(address)

    # creates a stub
    greeter_stub = GreeterStub(channel)

    # iterates n times
    for i in range(5):

        # send request and wait for response
        response = await greeter_stub.SayHello(HelloRequest(name="Fabito"))

        # print the received message
        logging.info(f"Received: {response.message}")

        # delay
        await sleep(1)

    # closes the channel
    await channel.close()

    logging.info("Execution finished!")


if __name__ == "__main__":

    # configures the logger
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s | %(message)s",
        level=logging.INFO,
    )

    # loads ssl certificates for encrypted and authenticated connections
    server_root = Path(__file__).parents[2] / "tls-certificates" / "server.crt"
    if not server_root.exists():
        raise FileNotFoundError(f"Unable to find server root file: {server_root}")

    # executes the main application
    run(
        main(
            host="localhost",
            port=9090,
            cert_root_path=server_root,
        )
    )
