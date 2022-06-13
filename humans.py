from glob import glob
from os import path
import os
import pathlib
import json
from cnf import Config
from main import USER_HOME


def config_test():
    # Config.
    return None


def list(*args, **kwargs):
    # print(kwargs['config']['paths']['src'])
    
    path_to_json = path.abspath(USER_HOME+kwargs['config']['paths']['src'])
    for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
        with open(path_to_json + "/" + file_name) as json_file:
            json_data = json.loads(json_file.read())      #takes JSON file and returns dictionary object
    print(json_data)
    
    # humans_data = {}
    
    # for employee in json_data:
    #     humans_data.append(employee["forter_id"])

def listOk(*args, **kwargs):
    
    path2teams = path.abspath(kwargs['config']['paths']['cgteams'])
    print(USER_HOME+kwargs['config']['paths']['cgteams'])   
    exit()
    