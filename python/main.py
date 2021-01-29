# import influxdb
from influxdb_client import InfluxDBClient, Point, WriteOptions, WriteApi
from influxdb_client.client.write_api import ASYNCHRONOUS
import pandas as pd
import numpy as np

# import keyboard module in same directory
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
# equivalent to SELECT * FROM coins and get the most recent values
query_coins = """
from(bucket: "coins/autogen")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "total_coins")
  |> last()
"""

coins_dataframe = _query_api.query_data_frame(query_coins)
print(coins_dataframe)
""" Setup keypad"""
kp = keypad()

try:
    while True:
        pass
except KeyboardInterrupt:
    _client.__del__()
    print('Exiting...')

