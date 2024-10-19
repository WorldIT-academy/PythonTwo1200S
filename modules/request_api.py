import requests
#
from .read_json import read_json
#
from .write_json import create_json
#
import json
#
data_api = read_json(name_file= 'config_api.json')
#
API_KEY = data_api['api_key']
#
CITY_NAME = data_api['city_name']
#
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
#
response = requests.get(URL)
#
if response.status_code == 200:
    #
    data_dict = json.loads(response.content)
    #
    create_json(name_json = 'config_weather.json', value_dict = data_dict)

    #
    print(json.dumps(data_dict, indent= 4))
else:
    print(f"Error: {response.status_code}")