import logging as logger
import os

import yaml
from termcolor import colored

import humans
from cnf import Config
from menu import menu

config = {}
USER_HOME = os.path.expanduser("~")  # USER_HOME = global variable


def main():

    c = Config()
    config = c.get_config()

    logger.basicConfig(
        level=config["logging"]["level"] if config["logging"]["enabled"] else 50
    )
    m = menu()

    m.add_option(
        "list",
        f"List JSON files in folder ({config['paths']['src']})",
        option_fn=human_list,
    )

    m.print_options()
    choice = m.get_choice()
    # print(choice)
    # choice['fn'](choice['fn_params'])


def human_list(*args, **kwargs):
    humans.list(*args, **kwargs)
    return None


if __name__ == "__main__":

    main()
