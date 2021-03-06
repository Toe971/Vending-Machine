import React, { useEffect, useState } from 'react';
import './App.css';
const {InfluxDB, Point} = require('@influxdata/influxdb-client')
const {url, token, org, bucket} = require('./env')




const influxDB = new InfluxDB({
  url: url,
  token: token,
});


const queryApi = influxDB.getQueryApi(org)
const fluxQuery =
 `from(bucket: ${bucket}/autogen)
 |> range(start: -30d)
 |> filter(fn: (r) => r._measurement == "total_coins")`

 // performs query and receive line table metadata and rows
// https://v2.docs.influxdata.com/v2.0/reference/syntax/annotated-csv/
queryApi.queryRows(fluxQuery, {
  next(row, tableMeta) {
    const o = tableMeta.toObject(row)
    // console.log(JSON.stringify(o, null, 2))
    console.log(
      ``
    )
  },
  error(error) {
    console.error(error)
    console.log('\nFinished ERROR')
  },
  complete() {
    console.log('\nFinished SUCCESS')
  },
})



function App() {
  return (
    <div className="App">
      <h1>Vending Machine</h1>
    </div>
  );
}

export default App;
