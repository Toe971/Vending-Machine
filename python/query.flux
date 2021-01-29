from(bucket: "coins/autogen")
  |> range(start: -30d)
  |> filter(fn: (r) => r._measurement == "total_coins")