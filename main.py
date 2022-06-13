from os import path
from menu import menu
import humans
from cnf import Config
import logging as logger
import yaml
from termcolor import colored

config = {}
USER_HOME = path.expanduser('~')    #USER_HOME = global variable

def main():

    c = Config()
    config = c.get_config()
    print(config)

    logger.basicConfig(
        level = config["logging"]["level"] if config["logging"]["enabled"] else 50
    )
    m = menu()

    m.add_option("list", f"List JSON files in folder ({config['paths']['src']})", option_fn=humans.list, params=[config])

    m.print_options()
    choice = m.get_choice()
    choice['fn'](config=config)


if __name__ == "__main__":
    
    main()
