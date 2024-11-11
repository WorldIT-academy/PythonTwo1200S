import customtkinter as ctk
from .main_frame import main_frame
import requests
import json

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
        CITY_NAME = "Dnipro"
        API_KEY = "f45b384d06f8d6558d2f50d57cd3220f"
        try:
            weather_data = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={API_KEY}&units=metric&cnt=4&lang=uk")
            hourly_data = json.loads(weather_data.content)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return

        print(json.dumps(hourly_data, indent = 4, ensure_ascii= False))


horizontal_scroll = WidgetHorizontalScroll(child_master= main_frame)
horizontal_scroll.request_api()