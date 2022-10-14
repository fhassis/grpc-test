import logging
import asyncio
import grpc

# adding autocode folder due to limitations in code generation
import sys
sys.path.append("autocode")

from autocode.greeter_pb2_grpc import add_GreeterServicer_to_server
from services.greeter_service import Greeter


async def serve(host: str, port: int) -> None:

    # creates the server
    server = grpc.aio.server()

    # adds the services to the server
    add_GreeterServicer_to_server(Greeter(), server)

    # configures the server port
    server.add_insecure_port(f"{host}:{port}")

    # starts the server
    logging.info(f"Starting server on {host}:{port}")
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
    logging.basicConfig(level=logging.DEBUG)

    # run the server
    asyncio.run(serve("localhost", 9090))
