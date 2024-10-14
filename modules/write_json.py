import json
import os

def create_json(name_json: str, value_dict: dict):
    path_file = os.path.abspath(__file__ + f'../../../static/{name_json}')
    with open(path_file, 'w') as file_for_save:
        json.dump(
            obj= value_dict, #
            fp= file_for_save, #
            ensure_ascii= False, #
            indent= 4 
        )