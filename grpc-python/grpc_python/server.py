import logging
from asyncio import run
from typing import Optional
from grpc.aio import server as grpc_server
from grpc import ssl_server_credentials
from pathlib import Path

# adding autocode folder due to limitations in code generation
import sys

sys.path.append("autocode")

from autocode.greeter_pb2_grpc import add_GreeterServicer_to_server
from services.greeter_service import Greeter


async def serve(
    host: str,
    port: int,
    key_path: Optional[Path] = None,
    chain_path: Optional[Path] = None,
) -> None:
    """
    Starts a grpc server.
    """
    address = f"{host}:{port}"

    # creates the server
    server = grpc_server()

    # adds the services to the server
    add_GreeterServicer_to_server(Greeter(), server)

    # configures the server port
    if key_path and chain_path:
        logging.info("Using secure ssl channel")
        private_key = open(key_path, "rb").read()
        certificate_chain = open(chain_path, "rb").read()
        server_credentials = ssl_server_credentials(((private_key, certificate_chain),))
        server.add_secure_port(address, server_credentials)
    else:
        logging.info("Using insecure channel")
        server.add_insecure_port(address)

    # starts the server
    logging.info(f"Starting server on {address}")
    await server.start()

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        # Shuts down the server with 0 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(0)


if __name__ == "__main__":

    # configures the logger
    logging.basicConfig(level=logging.INFO)

    # loads ssl certificates for encrypted and authenticated connections
    server_key = Path(__file__).parents[2] / "tls-certificates" / "server.key"
    if not server_key.exists():
        raise FileNotFoundError(f"Unable to find server key file: {server_key}")

    server_chain = Path(__file__).parents[2] / "tls-certificates" / "server.crt"
    if not server_chain.exists():
        raise FileNotFoundError(f"Unable to find server chain file: {server_chain}")

    # run the server
    run(
        serve(
            host="localhost",
            port=9091,
            key_path=server_key,
            chain_path=server_chain,
        )
    )
