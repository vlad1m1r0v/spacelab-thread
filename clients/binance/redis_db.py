import logging
from random import randint
from threading import Thread
from time import sleep

import redis
import requests


class BinanceRedisClient(Thread):
    def __init__(self, currency: str, period: int):
        Thread.__init__(self)
        self.__currency = currency
        self.__period = period
        self.__r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    def run(self):
        while True:
            response = requests.get(url="https://api.binance.com/api/v3/ticker/price",
                                    params={"symbol": self.__currency})
            price = response.json()["price"]
            random_integer = randint(1, 10)
            logging.info(f"from redis thread: {random_integer}")
            self.__r.set(self.__currency, price)
            sleep(self.__period)
