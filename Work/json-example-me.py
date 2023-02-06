from urllib.request import urlopen
import json
# import pprint

def readJson(url):
  '''
  open url that outputs json and read it
  '''
  u = urlopen(url)
  response = urlopen(url)
  
  data_load = json.loads(response.read())

  return data_load

def prettyPrint(json_object):
  pretty = json.dumps(json_object, indent=2)
  # pretty = pprint.pprint(json_object)

  print(pretty)


def write_json(new_data, url):
  data = readJson(url)
  data.append(new_data)
  output = json.dumps(data, indent = 2)
  print(output)

if __name__ == '__main__':
  
  url='https://data.binance.com/api/v3/ticker/24hr'
  # prettyPrint(readJson(url))
  
  new_symbol =   {
    "symbol": "CHEESE",
    "priceChange": "0.11900000",
    "priceChangePercent": "1.389",
    "weightedAvgPrice": "8.46937399",
    "prevClosePrice": "8.57300000",
    "lastPrice": "8.68500000",
    "lastQty": "2408.00000000",
    "bidPrice": "8.67500000",
    "bidQty": "22155.00000000",
    "askPrice": "8.68500000",
    "askQty": "15117.00000000",
    "openPrice": "8.56600000",
    "highPrice": "9.16900000",
    "lowPrice": "7.80200000",
    "volume": "64747107.00000000",
    "quoteVolume": "548367463.73400000",
    "openTime": 1675630916932,
    "closeTime": 1675717316932,
    "firstId": 329719,
    "lastId": 401785,
    "count": 72067
  }
  
  write_json(new_symbol, url)