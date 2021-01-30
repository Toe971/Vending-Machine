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
""" print(coins_dataframe.to_string()) """
# use a better way for indexing in the future, i.e. use pd methods
coins_key = coins_dataframe['_field'].to_list()
coins_list = coins_dataframe['_value'].to_list()
# shape of coin_dict: {'fifty_cents': 1000, 'one_dollar': 1000, 'ten_cents': 1000, 'twenty_cents': 1000}
coin_dict = dict(zip(coins_key, coins_list))
print(coin_dict)


query_drinks = """
from(bucket: "coins/autogen")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "total_drinks")
  |> last()
"""
drinks_dataframe = _query_api.query_data_frame(query_drinks)
""" print(drinks_dataframe.to_string()) """
drinks_key = drinks_dataframe['_field'].to_list()
drinks_list = drinks_dataframe['_value'].to_list()
drinks_dict = dict(zip(drinks_key, drinks_list))
# shape of drinks_dict: {'drink_one': 50, 'drink_three': 50, 'drink_two': 50}
print(drinks_dict)


def vending_logic():
    # REFACTOR EVERYTHING TOMORROW damn tired
    kp = keypad()
    flag = False
    digit = None
    coin_alphabet = ["A", "B", "C", "D"]
    coin_integer = [10, 20, 50, 100]
    # alphabet are dict keys and integer are dict values
    coin_alphabet_dict = dict(zip(coin_alphabet, coin_integer))
    drink_digits = [1, 2, 3]
    drink_prices = [70, 80, 120]
    # similar below
    drink_prices_dict = dict(zip(drink_digits, drink_prices))
    print("Press A, B, C, D to select 10 cents, 20 cents, 50 cents and 1 dollar respectively.")
    print()
    print('Press 1 for drink_1, 2 for drink_2, 3 for drink_3')
    print(f'Prices are: {drink_prices_dict[1]} cents, {drink_prices_dict[2]} cents, and {drink_prices_dict[3] // 100} dollar {drink_prices_dict[3] % 100} cents respectively')
    # import from keyboard.py later? hardcode for now
    # refactor after feeling less tired 

    # helper function to sum up coins inputted so far
    def sum_up_list(list):
        sum = 0
        for i in list:
            sum += i
        return sum

    sum_list = []
    accumulated_sum = 0
    change = 0
    # if drink_three_bool is 1, means that can pay for all drinks
    drink_one_bool = 0
    drink_two_bool = 0
    drink_three_bool = 0
    while flag != True:
        digit = kp.getKey()
        time.sleep(0.3)
        # for now bool will keep adding += 1 whenever user inputs more than needed i.e. if add till 2 dollars
        # need to change the logic if not remove the flag, or instead of += just assign i.e. = 
        # seems that assign will not be in scope, as the bool is defined inside the function
        # maybe need to use global drink_one_bool etc.
        if digit in coin_alphabet:
            sum_list.append(coin_alphabet_dict[digit])
            print(sum_list)
            accumulated_sum += coin_alphabet_dict[digit]
            print(accumulated_sum)
            if accumulated_sum < drink_prices[0]:
                print("Not enough coins deposited yet.")
            elif accumulated_sum < drink_prices[1]:
                print("Sum is enough for drink_1")
                drink_one_bool += 1
            elif accumulated_sum < drink_prices[2]:
                print("Sum is enough for drink_2")
                drink_two_bool += 1
            elif accumulated_sum >= drink_prices[2]:
                print("Sum is enough for all drinks!")
                drink_three_bool += 1
        # when user presses purchase button i.e. 1, 2, 3
        if digit in drink_digits:
            final_sum = sum_up_list(sum_list)
            if final_sum < drink_prices_dict[digit]:
                print("Not enough deposited for the selected drink!")
            else:
                # deduct the dispensed drink from drinks_list
                # add logic here
                change = 0
                for i in sum:
                    if i == 10:
                        coins_list[0] += 1
                    elif i == 20:
                        coins_list[1] += 1
                    elif i == 50:
                        coins_list[2] += 1
                    elif i == 100:
                        coins_list[3] += 1
                    sum.pop(i)
                if len(sum) != 0:
                    print('Dispensing change...')
                    for i in sum:
                        if i == 10:
                            coins_list[0] -= 1
                        elif i == 20:
                            coins_list[1] -= 1
                        elif i == 50:
                            coins_list[2] -= 1
                        elif i == 100:
                            coins_list[3] -= 1
                        sum.pop(i)

                    

            print(f"Dispensing drink{digit}...")




""" Setup keypad"""


try:
    while True:
        vending_logic()
except KeyboardInterrupt:
    _client.__del__()
    print('Exiting...')

