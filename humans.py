import json
import os
from glob import glob
from os import path

from cnf import Config
from main import USER_HOME
from menu import menu

db = {}


def list():
    c = Config()
    config = c.get_config()

    source_path = os.path.join(USER_HOME, config["paths"]["src"])
    for file in glob(f"{source_path}/*.json"):
        with open(file, "r") as json_file:
            data = json.loads(json_file.read())
            if "forter_id" in data:
                db[data["forter_id"]] = data

    humans_menu = menu()
    for item in db:
        humans_menu.add_option(item, item)

    humans_menu.print_options()

    # path_to_json = path.abspath(USER_HOME+kwargs['config']['paths']['src'])
    # for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    #     with open(path_to_json + "/" + file_name) as json_file:
    #         json_data = json.loads(json_file.read())      #takes JSON file and returns dictionary object
    # print(json_data)

    # humans_data = {}

    # for employee in json_data:
    #     humans_data.append(employee["forter_id"])


def listOk(*args, **kwargs):

    path2teams = path.abspath(kwargs["config"]["paths"]["cgteams"])
    print(USER_HOME + kwargs["config"]["paths"]["cgteams"])
    exit()
