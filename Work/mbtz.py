from urllib.request import urlopen
import json
import certifi

def open_data(url):
    with urlopen(url) as response:
        body = response.read()
        output = json.loads(body)
        print(output)

def main():
    mbta_json_url = 'https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/rest/services/Rapid_Transit_and_Bus_Prediction_Accuracy_Data_v2/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson'
    open_data(mbta_json_url)

if __name__ == '__main__':
    main()