import logging
from asyncio import sleep, run
from typing import Optional
from grpc.aio import insecure_channel, secure_channel
from grpc import ssl_channel_credentials
from pathlib import Path
import sys

# adding autocode folder due to limitations in code generation
import sys

sys.path.append("autocode")

from autocode.greeter_pb2_grpc import GreeterStub
from autocode.greeter_pb2 import HelloRequest


async def main(
    host: str,
    port: int,
    tls_cert_path: Optional[Path] = None,
) -> None:
    """
    Interacts to a grpc server.
    """
    address = f"{host}:{port}"

    # creates the communication channel
    if tls_cert_path:
        logging.info("Using secure ssl channel")
        server_credentials = open(tls_cert_path, "rb").read()
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

    if len(sys.argv) == 2 and sys.argv[1] == "--tls":
        # loads ssl certificates for encrypted and authenticated connections
        tls_cert = Path(__file__).parents[2] / "tls-certificates" / "cert.pem"
        if not tls_cert.exists():
            raise FileNotFoundError(f"Unable to find server root file: {tls_cert}")

    else:
        # uses insecure channel
        tls_cert = None

    # executes the main application
    run(
        main(
            host="localhost",
            port=9090,
            tls_cert_path=tls_cert,
        )
    )
