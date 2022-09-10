from mt5_grpc.services.metatrader.client import MetaTraderClient
from grpc_autocode.Symbols_pb2_grpc import SymbolsServiceServicer
from grpc_autocode.Symbols_pb2 import SymbolInfo, SymbolInfosList, SymbolTicker


class SymbolsService(SymbolsServiceServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetSymbolInfos(self, request, context):
        """
        Gets an array of symbol infos.
        """
        # get symbol infos from server
        symbol = request.symbol
        if symbol:
            raw_data = [self.mt_client.get_symbol_info(symbol)]
        else:
            raw_data = self.mt_client.get_symbol_infos()

        # convert and return SymbolInfos
        return SymbolInfosList(symbolInfos=[
            SymbolInfo(
                symbol=data.name,
                baseCurrency=data.currency_base,
                quotedCurrency=data.currency_profit,
                contractSize=data.trade_contract_size,
                digits=data.digits,
                tickSize=data.trade_tick_size,
                volumeMin=data.volume_min,
                volumeMax=data.volume_max,
                volumeStep=data.volume_step,
                swapMode=data.swap_mode,
                swapLong=data.swap_long,
                swapShort=data.swap_short,
                swap3days=data.swap_rollover3days,
            ) for data in raw_data
        ])

    async def GetSymbolTicker(self, request, context):
        """
        Gets ticker information of a given symbol.
        """
        # get symbol ticker from the server
        raw_data = self.mt_client.get_symbol_ticker(request.symbol)

        # convert and return SymbolTicker
        return SymbolTicker(
            time=raw_data.time_msc,
            ask=raw_data.ask,
            bid=raw_data.bid,
            last=raw_data.last,
            volume=raw_data.volume
        )