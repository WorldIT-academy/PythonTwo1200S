import customtkinter
from ..read_json import read_json
from .mainframe_windows import city_frame
#
current_position = customtkinter.CTkLabel(
    master= city_frame,
    text= "Поточна позицiя",
    font= ("Arial", 16, "bold"),
    justify= 'left',
    anchor= 'w'  # left justify the text in the label.
    
)
# 
current_position.place(x= 14, y= 8)