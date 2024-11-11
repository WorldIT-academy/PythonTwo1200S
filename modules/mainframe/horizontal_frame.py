import customtkinter as ctk
from .horizontal_scroll import horizontal_scroll

class HourlyWeather(ctk.CTkFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master= child_master,
            width= 50,
            height= 230,
            fg_color= "#5da7b1",
            # border_width= 2,
            **kwargs
        )
        self.pack(anchor= "w", padx= 20 )
        self.TIME = ctk.CTkLabel(
           master = self,
           text= "Час",
           font= ("Arial", 24, "bold"),
        #    fg_color= "#FFFFFF"
        )
        self.TIME.pack(anchor = "center", pady = 10)
        
hourly_weather = HourlyWeather(child_master = horizontal_scroll)