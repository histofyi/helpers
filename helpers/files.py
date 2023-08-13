from typing import Dict, List, Tuple, Union
import json
import os
from pathlib import Path


def create_folder(folder_path:str, verbose:bool) -> str:
    """
    This function creates the folder path if it does not already exist 
    
    Args:
        folder_path (str): the full path to the folder
        verbose (bool): whether the function should echo to the terminal if this argument is set to True
    
    Returns:
        str: the status of the folder e.g. created, already in existence
    """

    # check if the folder exists
    if not os.path.exists(folder_path):
        # if it doesn't exist, set folder_status to `folders_created`
        folder_status = 'folders_created'
        # create the folder and any parent folders needed
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        # if verbose is set to True, send a message to the terminal
        if verbose:  
            console.print (f"{folder_path} created")  
    else:
        # if it does exist, set folder_status to `folders_in_existence`
        folder_status = 'folders_in_existence'

        # if verbose is set to True, send a message to the terminal
        if verbose:
            console.print (f"{folder_path} already exists")  
    return folder_status



def load_constants(config:Dict, constants_name:str) -> Dict:
    """
    This function returns a dictionary of constants contained in a constants file in the constants directory specified in the config
    
    Args:
        constants_name (str): the name of the constantts dictionary

    Returns:
        Dict: the dictionary of constants
    
    """
    filepath = f'{config["PATHS"]["CONSTANTS"]}/{constants_name}.json'
    json_data = read_json(filepath)
    return json_data


def read_json(filepath:str) -> Union[Dict,List]:
    with open(filepath, 'r') as infile:
        json_data = json.load(infile)
    return json_data
    

def write_json(filepath:str, contents:Union[List,Dict], verbose:bool=False, pretty:bool=False) -> bool:
    try:
        with open(filepath, 'w') as outfile:
            if pretty:
                outfile.write(json.dumps(contents, sort_keys=True, indent=4))
            else:
                outfile.write(json.dumps(contents, sort_keys=True))
        if verbose:
            print (f'JSON file \'{filepath}\' written')
        return True
    except:
        return False


def write_file(filepath:str, contents:str, verbose:bool=False):
    with open(filepath,'w') as outfile:
        outfile.write(contents)
    if verbose:
        print (f'String file \'{filepath}\' written')


def write_step_tmp_output(tmp_folder:str, function_name:str, contents:Union[List, Dict], datehash:str, verbose:bool=False):
    tmp_output_directory = f"{tmp_folder}/steps/{function_name}"
    create_folder(tmp_output_directory, verbose=False)
    filepath = f"{tmp_output_directory}/output-{datehash}.json"
    write_json(filepath, contents, pretty=True)
    if verbose:
        print (f'Temporary output file \'{filepath}\' written') 