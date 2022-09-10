from datetime import datetime, timezone

from mt5_grpc.services.metatrader.client import MetaTraderClient
from grpc_autocode.ServerInfo_pb2_grpc import ServerInfoServicer
from grpc_autocode.ServerInfo_pb2 import ServerTimeRes, MarketWatchRes, MarketWatchListRes


class ServerInfo(ServerInfoServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetServerTime(self, request, context):
        """
        Returns the server time in UTC miliseconds.
        """
        server_time = int(datetime.now(timezone.utc).timestamp() * 1000)
        terminal_info = self.mt_client.get_terminal_info()
        terminal_ping = round(terminal_info.ping_last / 1000, 2)
        return ServerTimeRes(serverTime=server_time, terminalPing=terminal_ping)

    async def AddToMarketWatch(self, request, context):
        """
        Adds a symbol into Market Watch
        """
        status = self.mt_client.update_market_watch(request.symbol, True)
        return MarketWatchRes(status=status)

    async def RemoveFromMarketWatch(self, request, context):
        """
        Removes a symbol from Market Watch
        """
        status = self.mt_client.update_market_watch(request.symbol, False)
        return MarketWatchRes(status=status)

    async def GetMarketWatch(self, request, context):
        """
        Get Market Watch symbol list
        """
        all_symbols = self.mt_client.get_symbols_info()
        market_watch = [item.name for item in filter(lambda x: x.visible, all_symbols)]
        return MarketWatchListRes(symbols=market_watch)
