import logging
from grpc.aio import server
from asyncio import run

from mt5_grpc.services.metatrader.client import MetaTraderClient
from grpc_autocode.ServerInfo_pb2_grpc import add_ServerInfoServicer_to_server
from grpc_autocode.Candles_pb2_grpc import add_CandleServiceServicer_to_server
from grpc_autocode.Orders_pb2_grpc import add_OrdersServiceServicer_to_server
from grpc_autocode.Positions_pb2_grpc import add_PositionsServiceServicer_to_server
from grpc_autocode.Deals_pb2_grpc import add_DealsServiceServicer_to_server
from grpc_autocode.Symbols_pb2_grpc import add_SymbolsServiceServicer_to_server
from grpc_autocode.Account_pb2_grpc import add_AccountServiceServicer_to_server

from mt5_grpc.services.server_info import ServerInfo
from mt5_grpc.services.candles_service import CandleService
from mt5_grpc.services.orders_service import OrdersService
from mt5_grpc.services.positions_service import PositionsService
from mt5_grpc.services.deals_service import DealsService
from mt5_grpc.services.symbols_service import SymbolsService
from mt5_grpc.services.account_service import AccountService


async def serve(host: str, port: int):
    """
    Starts the gRPC server.
    """
    # initializes metatrader terminal
    logging.info("Initializing MetaTrader terminal")
    mt_client = MetaTraderClient()

    # creates the grpc server
    grpc_server = server()

    # adds the services into the server
    add_ServerInfoServicer_to_server(ServerInfo(mt_client), grpc_server)
    add_CandleServiceServicer_to_server(CandleService(mt_client), grpc_server)
    add_OrdersServiceServicer_to_server(OrdersService(mt_client), grpc_server)
    add_PositionsServiceServicer_to_server(PositionsService(mt_client), grpc_server)
    add_DealsServiceServicer_to_server(DealsService(mt_client), grpc_server)
    add_SymbolsServiceServicer_to_server(SymbolsService(mt_client), grpc_server)
    add_AccountServiceServicer_to_server(AccountService(mt_client), grpc_server)

    # configures the port
    listen_addr = f"{host}:{port}"
    grpc_server.add_insecure_port(listen_addr)

    # starts the server
    logging.info(f'Starting gRPC server on {listen_addr}')
    await grpc_server.start()

    try:
        await grpc_server.wait_for_termination()
    except KeyboardInterrupt:

        # shut down MetaTrader terminal
        logging.info("Shutting Down MetaTrader terminal")
        mt_client.dispose()

        # Shuts down the server with 0 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        logging.info(f'Stopping gRPC server on {listen_addr}')
        await grpc_server.stop(0)


if __name__ == "__main__":

    # configures the logger
    logging.basicConfig(
        format="%(asctime)s [ %(levelname)s ] %(name)s : %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=logging.DEBUG,
    )

    # loads server configuration
    host = "localhost"
    port = 9091

    # run the server
    run(serve(host, port))
