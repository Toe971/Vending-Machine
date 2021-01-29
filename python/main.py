# import influxdb
from influxdb_client import InfluxDBClient, Point, WriteOptions, WriteApi
from influxdb_client.client.write_api import ASYNCHRONOUS
import pandas as pd
import numpy as np

# import keypad class from keyboard.py in same directory
from keyboard import keypad
import time

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
print(coins_list)
# coin_dict has the quantity of coins left
coin_dict = {
    "ten_cents": coins_list[2],
    "twenty_cents": coins_list[3],
    "fifty_cents": coins_list[0],
    "one_dollar": coins_list[1]
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
print(drinks_list)
# drinks_dict has the quantity of drinks left
drinks_dict = {
    "drink_one": drinks_list[0],
    "drink_two": drinks_list[2],
    "drink_three": drinks_list[1]
}

def vending_logic():
    # REFACTOR EVERYTHING TOMORROW damn tired
    kp = keypad()
    flag = False
    digit = None
    print("Press A, B, C, D to select 10 cents, 20 cents, 50 cents and 1 dollar respectively.")
    print()
    print('Press 1 for drink_1, 2 for drink_2, 3 for drink_3')
    print('Prices are: 70 cents, 80 cents, and 1 dollar 20 cents respectively')
    # import from keyboard.py later? hardcode for now
    # refactor after feeling less tired 
    coin_alphabet = ["A", "B", "C", "D"]
    coin_alphabet_dict = {
        "A": 10,
        "B": 20,
        "C": 50,
        "D": 100
    }
    drink_digits = [1, 2, 3]
    drink_prices_dict = {
        1: 70, 
        2: 80, 
        3: 120
    }

    def sum_up_list(list):
        sum = 0
        for i in list:
            sum += i
        return sum

    sum = []
    accumulated_sum = 0
    # if drink_three_bool is 1, means that can pay for all drinks
    drink_one_bool = 0
    drink_two_bool = 0
    drink_three_bool = 0
    while flag != True:
        
        digit = kp.getKey()
        time.sleep(0.3)
        if digit in coin_alphabet:
            sum.append(coin_alphabet_dict[digit])
            print(sum)
            accumulated_sum = sum_up_list(sum)
            if accumulated_sum < 70:
                print("Not enough coins deposited yet.")
            elif accumulated_sum < 80:
                print("Sum is enough for drink_1")
                drink_one_bool += 1
            elif accumulated_sum < 120:
                print("Sum is enough for drink_2")
                drink_two_bool += 1
            elif accumulated_sum >= 120:
                print("Sum is enough for all drinks!")
                drink_three_bool += 1
        if digit in drink_digits:
            final_sum = sum_up_list(sum)
            if final_sum < drink_prices_dict[digit]:
                print("Not enough deposited for the selected drink!")
                break
            for i in sum:
                if i == 10:
                    coins_list[2] += 1
                elif i == 20:
                    coins_list[3] += 1
                elif i == 50:
                    coins_list[0] += 1
                elif i == 100:
                    coins_list[1] += 1
                sum.pop(i)
            if len(sum) != 0:
                print('Dispensing change...')
                for i in sum:
                    if i == 10:
                        coins_list[2] -= 1
                    elif i == 20:
                        coins_list[3] -= 1
                    elif i == 50:
                        coins_list[0] -= 1
                    elif i == 100:
                        coins_list[1] -= 1
                    sum.pop(i)

                    

            print(f"Dispensing drink{digit}...")




""" Setup keypad"""


try:
    while True:
        vending_logic()
except KeyboardInterrupt:
    _client.__del__()
    print('Exiting...')

