import customtkinter as ctk
from .horizontal_scroll import horizontal_scroll
from .image_weather import WeatherImage

class HourlyWeather(ctk.CTkFrame):
    def __init__(self, child_master: object, count: int= 0, **kwargs):
        self.COUNT = count
        ctk.CTkFrame.__init__(
            self,
            master= child_master,
            fg_color= "#5da7b1",
            **kwargs
        )
        # self.pack(anchor= "w", padx= 20 )
        self.grid(row= 0, column= self.COUNT)
        
        self.TIME = ctk.CTkLabel(
           master = self,
           text= "Час",
           font= ("Arial", 24, "bold"),
        )
        self.TIME.pack(anchor = "center", pady = 10)
        
        self.IMAGE = WeatherImage(
            child_master = self,
            name_file= 'config_forecaste.json',
            count= self.COUNT,
            size= (50, 50),
        )
        self.IMAGE.pack(anchor = "center", pady = 10)
        
for el in range(4):
    hourly_weather = HourlyWeather(child_master = horizontal_scroll, count= el)