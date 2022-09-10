from mt5_grpc.services.metatrader.client import MetaTraderClient
from mt5_grpc.services.metatrader.typings import Timeframe as MT_Timeframe
from grpc_autocode.Candles_pb2_grpc import CandleServiceServicer
from grpc_autocode.Candles_pb2 import Candle, Timeframe, CandleList


class CandleService(CandleServiceServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetLastCandles(self, request, context):
        """
        Gets an array of the last n candles.
        """
        # get candles from server
        raw_data = self.mt_client.get_candles(
            symbol=request.symbol,
            timeframe=grpc_to_mt5_timeframe(request.timeframe),
            count=request.amount
        )
        return CandleList(candles=[
            Candle(time=int(data[0]),
                   open=float(data[1]),
                   high=float(data[2]),
                   low=float(data[3]),
                   close=float(data[4]),
                   volume=int(data[5])  # 5 tick volume, 7 for real volume
                   ) for data in raw_data]
        )

    def GetCandlesSince(self, request, context):
        """
        Gets an array of the last candles since a given date.
        """
        raise NotImplementedError("GetCandlesSince not implemented.")


def grpc_to_mt5_timeframe(grpc_tf: Timeframe) -> MT_Timeframe:
    """
    Converts from gRPC Timeframe to MT5 Timeframe.
    """
    match grpc_tf:
        case Timeframe.M1:
            return MT_Timeframe.M1
        case Timeframe.M15:
            return MT_Timeframe.M15
        case Timeframe.H1:
            return MT_Timeframe.H1
        case Timeframe.H4:
            return MT_Timeframe.H4
        case Timeframe.D1:
            return MT_Timeframe.D1
        case _:
            raise NotImplementedError(f"Invalid timeframe: {grpc_tf}")
