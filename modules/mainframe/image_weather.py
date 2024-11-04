import customtkinter
from .main_frame import main_frame
import os
from ..read_json import read_json
import PIL.Image

class WeatherImage(customtkinter.CTkLabel):
    def __init__(self, child_master: object, **kwargs):
        customtkinter.CTkLabel.__init__(
            self, 
            master= child_master, 
            width= 245,
            height= 100,
            text= '',
            image= self.load_image(),
            **kwargs
        )
        self.place(x= 380, y= 170)
        
    def load_image(self):
        #
        weather_data = read_json(name_file= "config_weather.json")
        #
        image_weather = weather_data['weather'][0]['icon']
        #
        path_image = os.path.abspath(__file__ + f"/../../../media/images/{image_weather}.png")
        #
        return customtkinter.CTkImage(light_image= PIL.Image.open(path_image), size= (170, 160))
    
    
image = WeatherImage(child_master= main_frame)

