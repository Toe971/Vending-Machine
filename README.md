# Vending Machine Prototype

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app), and also
[Adafruit CircuitPython](https://github.com/adafruit/circuitpython)

## Installing and setup for InfluxDB

Go to [https://github.com/influxdata/influxdb-client-python](https://github.com/influxdata/influxdb-client-python) and follow the installation guide.
We are using not using InfluxDB 2.0+ and above for this vending machine demo as it has a pricing plan, and limited
functionality for open source buckets.
See [https://docs.influxdata.com/influxdb/v1.8/administration/config/](https://docs.influxdata.com/influxdb/v1.8/administration/config/) on how to set up environment variables and edit InfluxDB.
Launch InfluxDB's command line interface in the bash terminal of your choice with

```bash
influx -precision rfc3339
```

Then, create a database named coins. For more information, visit [https://docs.influxdata.com/influxdb/v1.8/query_language/manage-database/](https://docs.influxdata.com/influxdb/v1.8/query_language/manage-database/)
Enter the following code into the InfluxDB CLI:

```
CREATE DATABASE coins
```

finally, enter exit to quit the CLI.

```
exit
```

## Python Dependencies

The python script is intended to run on the Raspberry Pi.
libatlas library needs to be installed to overcome errors caused by installing pandas, as pandas
will fail to uninstall numpy.
See [https://numpy.org/doc/stable/user/troubleshooting-importerror.html?highlight=setup%20py](https://numpy.org/doc/stable/user/troubleshooting-importerror.html?highlight=setup%20py)
To install system-wide the required python dependencies:

```bash
sudo pip3 install adafruit-circuitpython-matrixkeypad
sudo pip3 install pandas
sudo apt-get install libatlas-base-dev
sudo pip3 install websockets
```

## To-do

- [x] Do this
- [ ] Read more and practise on rxpy and rxjs in preparation for InfluxDB querying and async py
- [ ] Read up on Rekognition AWS and other image detection technologies in the cloud
