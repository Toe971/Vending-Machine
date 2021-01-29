from influxdb_client import InfluxDBClient, Point, WriteOptions, WriteApi
from influxdb_client.client.write_api import ASYNCHRONOUS

# coin_dict are going to be the measurements
coin_dict = {
    "ten_cents": 1000,
    "twenty_cents": 1000,
    "fifty_cents": 1000,
    "one_dollar": 1000
}

drinks_dict = {
    "drink_one": 50,
    "drink_two": 50,
    "drink_three": 50
}

""" 

replace ID, PWD, ORG, and BUCKET with your own values. BUCKET is InfluxDB 2.0+ alias for database in InfluxDB 1.8+
see https://docs.influxdata.com/influxdb/v1.8/tools/api/

"""
InfluxDB_ID = ""
InfluxDB_PWD = ""
InfluxDB_ORG = ""
InfluxDB_BUCKET = "coins"

"""Initialize InfluxDBClient"""

_client = InfluxDBClient(url="http://localhost:8086",
                         token=f"{InfluxDB_ID}:{InfluxDB_PWD}", org=f"{InfluxDB_ORG}")
_write_client = _client.write_api(write_options=WriteOptions(ASYNCHRONOUS))
_query_api = _client.query_api()


""" Reference:
* _write_client.write("my-bucket", "my-org", [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"},
                                    "fields": {"water_level": 2.0}, "time": 2},
                                    {"measurement": "h2o_feet", "tags": {"location": "coyote_creek"},
                                    "fields": {"water_level": 3.0}, "time": 3}])

* _write_client.write("my-bucket", "my-org", Point("h2o_feet").tag("location", "coyote_creek").field("water_level", 4.0).time(4))
    _write_client.write("my-bucket", "my-org", [Point("h2o_feet").tag("location", "coyote_creek").field("water_level", 5.0).time(5),
                                    Point("h2o_feet").tag("location", "coyote_creek").field("water_level", 6.0).time(6)])
"""


_write_client.write(InfluxDB_BUCKET, InfluxDB_ORG, [{
                                                        "measurement": "total_coins", 
                                                        "tags": {"vending_one": "yishun"},
                                                        "fields": coin_dict
                                                    },
                                                    {
                                                        "measurement": "total_drinks", 
                                                        "tags": {"vending_one": "yishun"},
                                                        "fields": drinks_dict
                                                    }])

_client.__del__()
