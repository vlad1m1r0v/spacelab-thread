import asyncio
import logging
from threading import Thread
from time import sleep, localtime, strftime

import requests

from currency_model import Currency


class BinanceDbClient(Thread):
    def __init__(self, currency: str, period: int):
        Thread.__init__(self)
        self.__currency = currency
        self.__period = period

    def run(self):
        while True:
            response = requests.get(url="https://api.binance.com/api/v3/ticker/price",
                                    params={"symbol": self.__currency})
            price = response.json()["price"]
            t = localtime()
            current_time = strftime("%H:%M:%S", t)
            logging.info(f"from sqlite3 thread: {current_time}")
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(Currency.create(currency=self.__currency,
                                                    price=float(price)))
            loop.close()

            sleep(self.__period)
