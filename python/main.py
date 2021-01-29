# import influxdb
from influxdb_client import InfluxDBClient, Point, WriteOptions, WriteApi
from influxdb_client.client.write_api import SYNCHRONOUS
# import keyboard module in same directory
import keyboard


""" Setup InfluxDB client """
InfluxDB_ID = "jenius"
InfluxDB_PWD = "jeniuspassword"
InfluxDB_ORG = "admin"
InfluxDB_BUCKET = "IPCS/two_weeks"

_client = InfluxDBClient(url="http://localhost:8086",
                         token=f"{InfluxDB_ID}:{InfluxDB_PWD}", org=f"{InfluxDB_ORG}")
_write_client = _client.write_api(write_options=WriteOptions(batch_size=500,
                                                             flush_interval=10_000,
                                                             jitter_interval=2_000,
                                                             retry_interval=5_000,
                                                             max_retries=5,
                                                             max_retry_delay=30_000,
                                                             exponential_base=2))


_write_client.write(InfluxDB_BUCKET, InfluxDB_ORG, [{"measurement": "MOTION", "tags": {"SFR_No": "ONE"},
                                                             "fields": {"MOTION_BOOLEAN": motion_boolean}},
                                                            {"measurement": "BATTERY", "tags": {"SFR_No": "ONE"},
                                                             "fields": {
                                                                "BATTERY_CAPACITY": round(readCapacity(bus), 2),
                                                                "BATTERY_VOLTAGE": round(readVoltage(bus), 2)
                                                            }}])

""" Setup keypad"""


kp = keypad()
