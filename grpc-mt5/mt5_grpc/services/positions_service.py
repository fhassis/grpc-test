from mt5_grpc.services.metatrader.client import MetaTraderClient
from mt5_grpc.services.metatrader.typings import OrderType
from grpc_autocode.Positions_pb2_grpc import PositionsServiceServicer
from grpc_autocode.Positions_pb2 import Position, PositionsList, OpenPositionRes, ModifyPositionRes, ClosePositionRes, \
    PositionType


class PositionsService(PositionsServiceServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetPositions(self, request, context):
        """
        Gets an array of the current open positions.
        """
        # get orders from server
        raw_data = self.mt_client.get_positions(symbol=request.symbol)

        # convert and return orders
        return PositionsList(positions=[
            Position(
                id=data.ticket,
                symbol=data.symbol,
                type=data.type,
                price=data.price_open,
                sl=data.sl,
                tp=data.tp,
                volume=data.volume,
                time=data.time_msc,
                magic=data.magic,
                comment=data.comment
            ) for data in raw_data
        ])

    async def OpenPosition(self, request, context):
        """
        Opens a position.
        """
        ticket = self.mt_client.open_position(
            order_type=OrderType.BUY_MARKET if request.type == PositionType.LONG else OrderType.SELL_MARKET,
            symbol=request.symbol,
            volume=request.volume,
            sl=request.sl,
            tp=request.tp
        )
        return OpenPositionRes(ticket=ticket)

    async def ModifyPosition(self, request, context):
        """
        Modifies a position.
        """
        status = self.mt_client.modify_position(
            ticket=request.ticket,
            sl=request.sl,
            tp=request.tp
        )
        return ModifyPositionRes(status=status)

    async def ClosePosition(self, request, context):
        """
        Closes a position.
        """
        status = self.mt_client.close_position(ticket=request.ticket)
        return ClosePositionRes(status=status)
