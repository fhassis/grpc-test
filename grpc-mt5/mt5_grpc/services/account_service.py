from mt5_grpc.services.metatrader.client import MetaTraderClient
from grpc_autocode.Account_pb2_grpc import AccountServiceServicer
from grpc_autocode.Account_pb2 import AccounInfo, AccountStatus


class AccountService(AccountServiceServicer):

    def __init__(self, mt_client: MetaTraderClient):
        self.mt_client = mt_client

    async def GetAccountInfo(self, request, context):
        """
        Gets static account information.
        """
        raw_data = self.mt_client.get_account_info()

        # convert and return AccountInfo
        return AccounInfo(
            id=raw_data.login,
            broker=raw_data.company,
            currency=raw_data.currency,
            digits=raw_data.currency_digits
        )

    async def GetAccountStatus(self, request, context):
        """
        Gets dynamic account status.
        """
        raw_data = self.mt_client.get_account_info()

        # convert and return AccountStatus
        return AccountStatus(
            balance=raw_data.balance,
            equity=raw_data.equity,
            usedMargin=raw_data.margin,
            freeMargin=raw_data.margin_free
        )
