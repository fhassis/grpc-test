from mt5_grpc.services.metatrader.client import MetaTraderClient
from grpc_autocode.Orders_pb2_grpc import OrdersServiceServicer
from grpc_autocode.Orders_pb2 import Order, OrdersList


class OrdersService(OrdersServiceServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetOrders(self, request, context):
        """
        Gets an array of the current open orders.
        """
        # get orders from server
        raw_data = self.mt_client.get_orders(symbol=request.symbol)

        # convert and return orders
        return OrdersList(orders=[
            Order(
                id=data.ticket,
                symbol=data.symbol,
                type=data.type,
                price=data.price_open,
                sl=data.sl,
                tp=data.tp,
                volumeInitial=data.volume_initial,
                volumeCurrent=data.volume_current,
                time=data.time_setup_msc,
                expiration=data.time_expiration_msc,
                magic=data.magic,
                comment=data.comment
            ) for data in raw_data
        ])
