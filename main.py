from tortoise import run_async

from clients.binance import BinanceRedisClient, BinanceDbClient
from logger import init_logger
from sqlite3_connection import init_sqlite

init_logger()

run_async(init_sqlite())

binance_btc_db_client = BinanceDbClient(currency="BTCUSDT", period=2)
binance_ltc_redis_client = BinanceRedisClient(currency="LTCUSDT", period=3)

binance_btc_db_client.start()
binance_ltc_redis_client.start()
