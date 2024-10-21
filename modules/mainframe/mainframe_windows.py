import customtkinter 
from .main_frame import main_frame, HEIGHT

scrollable_frame = customtkinter.CTkScrollableFrame(
    master= main_frame, 
    width= 275, 
    height= HEIGHT,
    border_width= 3,
    border_color= '#000000',
    label_text= 'Scroll',
    orientation= 'vertical',
    fg_color= '#096C82'
)
# scrollable_frame.pack(fill='both', expand=True)
# main_frame.grid()
scrollable_frame.grid(row=0, column=0, sticky='nsew')
