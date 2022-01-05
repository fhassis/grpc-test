import logging
import asyncio
import grpc

from autocode.helloworld_pb2_grpc import add_GreeterServicer_to_server
from services.greeter_service import Greeter


async def serve() -> None:

    # creates the server
    server = grpc.aio.server()

    # adds the services to the server
    add_GreeterServicer_to_server(Greeter(), server)

    # configures the server port
    listen_addr = 'localhost:9090'
    server.add_insecure_port(listen_addr)

    # starts the server
    logging.info(f'Starting server on {listen_addr}')
    await server.start()

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        # Shuts down the server with 0 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(0)


if __name__ == '__main__':

    # configures the logger
    logging.basicConfig(level=logging.DEBUG)

    # run the server
    asyncio.run(serve())
