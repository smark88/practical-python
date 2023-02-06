import json
import urllib.request

def get_json_data(url):
    # Make a GET request to retrieve the JSON data
    response = urllib.request.urlopen(url)

    # Check if the request was successful
    if response.getcode() == 200:
        # Load the JSON data into a Python dictionary
        return json.loads(response.read().decode())
    else:
        print("Request failed with status code:", response.getcode())
        return None

def add_item_to_json(data, new_item):
    # Add a new item to the data
    data.append(new_item)
    return data

url = "https://data.binance.com/api/v3/ticker/24hr"
data = get_json_data(url)
new_item={
    "symbol": "CHEESE",
    "priceChange": "0.11900000",
    "priceChangePercent": "1.389",
    "weightedAvgPrice": "8.46937399"}

if data is not None:
    data = add_item_to_json(data, new_item)
    print(json.dumps(data, indent=4))
