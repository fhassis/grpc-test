import logging
from asyncio import run
from typing import Optional
from grpc.aio import server as grpc_server
from grpc import ssl_server_credentials
from pathlib import Path
import sys

# adding autocode folder due to limitations in code generation
import sys

sys.path.append("autocode")

from autocode.greeter_pb2_grpc import add_GreeterServicer_to_server
from services.greeter_service import Greeter


async def serve(
    host: str,
    port: int,
    private_key_path: Optional[Path] = None,
    tls_cert_path: Optional[Path] = None,
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
    if private_key_path and tls_cert_path:
        logging.info("Using secure ssl channel")
        private_key = open(private_key_path, "rb").read()
        certificate_chain = open(tls_cert_path, "rb").read()
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
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s | %(message)s",
        level=logging.INFO,
    )

    if len(sys.argv) == 2 and sys.argv[1] == "--tls":
        # loads ssl certificates for encrypted and authenticated connections
        private_key = Path(__file__).parents[2] / "tls-certificates" / "key.pem"
        if not private_key.exists():
            raise FileNotFoundError(f"Unable to find server key file: {private_key}")

        tls_cert = Path(__file__).parents[2] / "tls-certificates" / "cert.pem"
        if not tls_cert.exists():
            raise FileNotFoundError(f"Unable to find server chain file: {tls_cert}")

    else:
        # uses insecure channel
        private_key = None
        tls_cert = None

    # run the server
    run(
        serve(
            host="localhost",
            port=9090,
            private_key_path=private_key,
            tls_cert_path=tls_cert,
        )
    )
