/** InfluxDB v2 URL */
const url = process.env['INFLUX_URL'] || 'http://localhost:8086'
/** InfluxDB authorization token */
const token = process.env['INFLUX_TOKEN'] || ''
/** Organization within InfluxDB  */
const org = process.env['INFLUX_ORG'] || ''
/**InfluxDB bucket used in examples  */
const bucket = process.env['BUCKET'] || 'coins'
// ONLY onboarding example
/**InfluxDB user  */
const username = ''
/**InfluxDB password  */
const password = ''

module.exports = {
  url,
  token,
  org,
  bucket,
  username,
  password,
}