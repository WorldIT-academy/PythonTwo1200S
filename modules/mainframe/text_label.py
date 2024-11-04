import customtkinter
from ..read_json import read_json
from .mainframe_windows import scrollable_frame
#
class CityCurrent(customtkinter.CTkFrame):
    def __init__(self, master: object, name_city: str, config_weather: dict, **kwargs):
        super().__init__(
            master= master, 
            width= 245,
            height= 100,
            border_width= 2,
            border_color= '#FFFFFF',
            corner_radius= 20,
            fg_color= '#4599A4',
            **kwargs
        )
        # 
        self.pack(anchor= 'center', expand=True, pady = 10)
        self.CONFIG_WEATHER = read_json(name_file= config_weather)
        #
        self.CURRENT_POSITION = customtkinter.CTkLabel(
            master= self,
            text= "Поточна позицiя",
            font= ("Arial", 16, "bold"),
            justify= 'left',
        )
        self.CURRENT_POSITION.place(x= 14, y= 8)
        #
        self.NAME_CITY = customtkinter.CTkLabel(
            master= self,
            text= name_city,
            font= ("Arial", 12, "bold"),
            justify= 'left',
        )
        self.NAME_CITY.place(x= 14, y= 33)
        #
        self.TEMP = customtkinter.CTkLabel(
            master= self,
            text= f"{int(self.CONFIG_WEATHER['main']['temp'])}°",
            font= ("Arial", 50, "bold"),
        )
        self.TEMP.place(x= 160, y= 8)

#
city_name = read_json(name_file= "config_api.json")['city_name']
#

for el in range(10):
    city_frame = CityCurrent(
        master= scrollable_frame, 
        name_city= city_name, 
        config_weather= 'config_weather.json',
)