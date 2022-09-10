import logging
from datetime import datetime, timezone
import MetaTrader5 as mt5

from mt5_grpc.services.metatrader.typings import TerminalInfo, Timeframe, SymbolInfo, AccountInfo, Ticker, OrderType


class MetaTraderClient:
    """
    Client to interact with the MetaTrader 5 terminal.
    """
    connected: bool

    def __init__(self) -> None:
        self.initialize()

    @staticmethod
    def initialize() -> None:
        """
        Initializes and connects with the default MetaTrader 5 installation.
        If the terminal is closed, this function opens it.
        """
        if not mt5.initialize():
            msg = f"Terminal initialization failure: {mt5.last_error()}"
            logging.error(msg)
            raise Exception(msg)

    @staticmethod
    def dispose() -> None:
        """
        Closes the connection with the MetaTrader 5 terminal.
        If the terminal was opened during connect, this function closes it.
        """
        mt5.shutdown()

    @staticmethod
    def get_terminal_info() -> TerminalInfo:
        """
        Get the connected MetaTrader 5 client terminal status and settings.
        https://www.mql5.com/en/docs/integration/python_metatrader5/mt5terminalinfo_py
        """
        return mt5.terminal_info()

    @staticmethod
    def get_candles(symbol: str, timeframe: Timeframe, count: int, from_date: datetime = None):
        """
        Get the candles from MetaTrader as a numpy array. Datetime shall be in UTC. If none, "now" is created.
        The order of data is: time, open, high, low, close, tick_volume, spread and real_volume
        """
        from_date = from_date if from_date else datetime.now(timezone.utc)
        return mt5.copy_rates_from(symbol, timeframe.value, from_date, count)

    @staticmethod
    def get_orders(symbol: str = None):
        if symbol:
            raw_data = mt5.orders_get(symbol=symbol)
        else:
            raw_data = mt5.orders_get()
        return raw_data if raw_data else []

    @staticmethod
    def get_positions(symbol: str = None):
        if symbol:
            raw_data = mt5.positions_get(symbol=symbol)
        else:
            raw_data = mt5.positions_get()
        return raw_data if raw_data else []

    @staticmethod
    def get_position(ticket: int):
        raw_data = mt5.positions_get(ticket=ticket)
        return raw_data[0] if raw_data else None

    @staticmethod
    def get_deals(from_date: datetime, to_date: datetime = None):
        to_date = to_date if to_date else datetime.now(timezone.utc)
        return mt5.history_deals_get(from_date, to_date)

    @staticmethod
    def get_account_info() -> AccountInfo:
        return mt5.account_info()

    @staticmethod
    def get_symbol_info(symbol: str = None) -> SymbolInfo:
        return mt5.symbol_info(symbol)

    @staticmethod
    def get_symbol_infos() -> list[SymbolInfo]:
        return mt5.symbols_get()

    @staticmethod
    def get_symbol_ticker(symbol: str) -> Ticker:
        return mt5.symbol_info_tick(symbol)

    @staticmethod
    def update_market_watch(symbol: str, enable: bool) -> bool:
        return mt5.symbol_select(symbol, enable)

    @staticmethod
    def get_last_error():
        return mt5.last_error()

    @staticmethod
    def _send_request(request):
        """
        Handles the requests to the MetaTrader terminal.
        """
        # send the request to the trade server
        result = mt5.order_send(request)

        # check the result
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logging.error(f"order_send failed. retcode={result.retcode}")
            result_dict = result._asdict()
            for field in result_dict.keys():
                print(f"   {field}={result_dict[field]}")
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print(f"       traderequest: {tradereq_filed}={traderequest_dict[tradereq_filed]}")
        else:
            logging.info(f"order_send done. {result}")
            logging.info(f"   opened position with POSITION_TICKET={result.order}")

    @staticmethod
    def open_position(order_type: OrderType, symbol: str, volume: float, price: float = None, sl: float = 0.0,
                      tp: float = 0.0, comment: str = "", magic: int = 0) -> int:
        """
        Opens a position.
        """
        # check order type
        if (order_type != OrderType.BUY_MARKET) and (order_type != OrderType.SELL_MARKET):
            raise ValueError(f"Invalid order type for opening position: {order_type}")

        # get the price if not provided
        if not price:
            tick = MetaTraderClient.get_symbol_ticker(symbol)
            price = tick.ask if order_type == OrderType.BUY_MARKET else tick.bid

        # form request object
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 20,
            "magic": magic,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK
        }

        # send the request to the trade server
        result = mt5.order_send(request)

        # check the result
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logging.error(f"open_position failed. retcode={result.retcode} | comment: {result.comment}")
            return 0
        else:
            logging.info(f"Position opened successfully. Ticket: {result.order}")
            return result.order

    @staticmethod
    def close_position(ticket: int) -> bool:
        """
        Closes the position with the given ticket.
        """
        # get the position
        position = MetaTraderClient.get_position(ticket)

        # check if position still exists
        if not position:
            logging.error(f"Unable to find position {ticket}")
        else:
            # define order type based on the current position
            order_type = mt5.ORDER_TYPE_BUY if position.type == mt5.POSITION_TYPE_SELL else mt5.ORDER_TYPE_SELL

            # get tick data to find current ask and bid
            tick = MetaTraderClient.get_symbol_ticker(position.symbol)

            # get the current price according to the order type
            price = tick.ask if order_type == OrderType.BUY_MARKET else tick.bid

            # form the request object
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": position.symbol,
                "volume": position.volume,
                "type": order_type,
                "position": position.ticket,
                "price": price,
                "deviation": 20,
                "magic": position.magic,
                "comment": position.comment,
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_FOK,
            }

            # send the request to the trade server
            result = mt5.order_send(request)

            # check the result
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logging.error(f"close_position failed. retcode={result.retcode} | comment: {result.comment}")
                return False
            else:
                logging.info(f"Position {ticket} closed successfully")
                return True

    @staticmethod
    def modify_position(ticket: int, sl: float = None, tp: float = None) -> bool:
        """
        Modifies a given position.
        """
        # get the position
        position = MetaTraderClient.get_position(ticket)

        # check if position still exists
        if not position:
            logging.error(f"Unable to find position {ticket}")
        else:
            # form the request object
            request = {
                "action": mt5.TRADE_ACTION_SLTP,
                "symbol": position.symbol,
                "sl": position.sl if sl is None else sl,
                "tp": position.tp if tp is None else tp,
                "position": position.ticket,
            }

            # send the request to the trade server
            result = mt5.order_send(request)

            # check the result
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logging.error(f"modify_position failed. retcode={result.retcode} | comment: {result.comment}")
                return False
            else:
                logging.info(f"Position {ticket} modified successfully")
                return True
