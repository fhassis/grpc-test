from mt5_grpc.services.metatrader.client import MetaTraderClient
from grpc_autocode.Deals_pb2_grpc import DealsServiceServicer
from grpc_autocode.Deals_pb2 import Deal, DealsList


class DealsService(DealsServiceServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetDeals(self, request, context):
        """
        Gets an array of deals.
        """
        # get deals from server
        from_date = request.fromDate
        to_date = request.toDate if request.toDate else None
        raw_data = self.mt_client.get_deals(from_date=from_date, to_date=to_date)

        # convert and return deals
        return DealsList(deals=[
            Deal(
                id=data.position_id,
                symbol=data.symbol,
                type=data.type,
                price=data.price,
                volume=data.volume,
                profit=data.profit,
                swap=data.swap,
                fee=data.fee,
                time=data.time_msc,
                magic=data.magic,
                comment=data.comment,
                reason=data.reason
            ) for data in raw_data
        ])
