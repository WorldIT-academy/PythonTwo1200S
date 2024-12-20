import customtkinter
from .main_frame import main_frame
import os
from ..read_json import read_json
import PIL.Image

class WeatherImage(customtkinter.CTkLabel):
    def __init__(self, child_master: object, name_file: str, count: int= 0, size: tuple= [int, int], **kwargs):
        self.NAME_FILE = name_file
        self.COUNT = count
        self.SIZE = size
        customtkinter.CTkLabel.__init__(
            self, 
            master= child_master, 
            width= 245,
            height= 100,
            text= '',
            image= self.load_image(),
            **kwargs
        )
        
    def load_image(self):
        #
        weather_data = read_json(name_file= self.NAME_FILE)
        #
        if 'weather' in self.NAME_FILE:
            image_weather = weather_data['weather'][0]['icon']
        elif 'forecaste' in self.NAME_FILE:
            image_weather = weather_data['list'][self.COUNT]['weather'][0]['icon']
        #
        path_image = os.path.abspath(__file__ + f"/../../../media/images/{image_weather}.png")
        #
        return customtkinter.CTkImage(light_image= PIL.Image.open(path_image), size= self.SIZE)
    
    
image = WeatherImage(child_master= main_frame, name_file= 'config_weather.json', size= (170, 160))
image.place(x= 380, y= 170)

