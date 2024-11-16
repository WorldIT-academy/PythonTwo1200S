import customtkinter as ctk
from .main_frame import main_frame
import requests
import json
from ..write_json import create_json
from ..read_json import read_json

class WidgetHorizontalScroll(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self,
            master = child_master,
            width = 820,
            height = 240,
            border_color = "#FFFFFF",
            border_width = 5,
            corner_radius = 20,
            # label_text = "Захід сонця",
            fg_color = "#5DA7B1",
            orientation = "horizontal",
            **kwargs
        )
        self.place(x = 325, y = 430)
    #
    def request_api(self ):
        data_api = read_json(name_file= 'config_api.json')
        CITY_NAME = data_api['city_name']
        API_KEY = data_api['api_key']
        try:
        # url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric&cnt=4&lang=uk".format(CITY_NAME, API_KEY)
            weather_data = requests.get(url = data_api['url_forecast'].format(CITY_NAME, API_KEY))
            hourly_data = json.loads(weather_data.content)
            create_json(name_json= "config_forecaste.json", value_dict= hourly_data)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return

        print(json.dumps(hourly_data, indent = 4, ensure_ascii= False))


horizontal_scroll = WidgetHorizontalScroll(child_master= main_frame)
horizontal_scroll.request_api()