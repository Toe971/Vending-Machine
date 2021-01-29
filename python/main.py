# import influxdb
from influxdb_client import InfluxDBClient, Point, WriteOptions, WriteApi
from influxdb_client.client.write_api import ASYNCHRONOUS
import pandas as pd
import numpy as np

# import keypad class from keyboard.py in same directory
from keyboard import keypad


""" Setup InfluxDB client """
InfluxDB_ID = ""
InfluxDB_PWD = ""
InfluxDB_ORG = ""
InfluxDB_BUCKET = "coins"

_client = InfluxDBClient(url="http://localhost:8086",
                         token=f"{InfluxDB_ID}:{InfluxDB_PWD}", org=f"{InfluxDB_ORG}")
_write_client = _client.write_api(write_options=WriteOptions(ASYNCHRONOUS))
_query_api = _client.query_api()
# equivalent to USE coins, SELECT * FROM total_coins and get the most recent values for the last 30 days
query_coins = """
from(bucket: "coins/autogen")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "total_coins")
  |> last()
"""
coins_dataframe = _query_api.query_data_frame(query_coins)
print(coins_dataframe.to_string())
coins_list = coins_dataframe['_value'].to_list()
coin_dict = {
    "ten_cents": coins_list[0],
    "twenty_cents": coins_list[1],
    "fifty_cents": coins_list[2],
    "one_dollar": coins_list[3]
}

query_drinks = """
from(bucket: "coins/autogen")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "total_drinks")
  |> last()
"""
drinks_dataframe = _query_api.query_data_frame(query_drinks)
print(drinks_dataframe.to_string())
drinks_list = drinks_dataframe['_value'].to_list()
drinks_dict = {
    "drink_one": drinks_list[0],
    "drink_two": drinks_list[1],
    "drink_three": drinks_list[2]
}

def vending_logic():
    kp = keypad()
    flag = False
    digit = None
    print("Press A, B, C, D to select 10 cents, 20 cents, 50 cents and 1 dollar respectively.")
    while flag != True:
        digit = kp.getKey()
        print(digit)   

""" Setup keypad"""


try:
    while True:
        vending_logic()
except KeyboardInterrupt:
    _client.__del__()
    print('Exiting...')

