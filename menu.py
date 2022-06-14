import logging as logger
from typing import Callable

from termcolor import colored


class menu:
    
    def __init__(self, options = {}):
        self.options = options

    def add_option(
        self, option_id, option_text: str, option_fn=None, params=None
    ) -> None:
        self.options[option_id] = {
            "option_text": option_text,
            "fn": option_fn,
            "fn_params": params,
        }
        logger.debug("Added option: ")
        logger.debug(self.options[option_id])

    def get_options(self):
        return self.options

    def print_options(
        self,
        noback: bool = False,
        back_fn=exit,
        back_fn_params=[0],
        back_description: str = "Exit",
        back_key: str = "x",
    ):
        if not noback:
            self.add_back_option(back_key, back_description, back_fn, back_fn_params)
        i = 1
        for option in self.options:
            print(f"{i}. {self.options[option]['option_text']}")
            i += 1

    def get_choice(self, text: str = "Enter your choice: "):
        try:
            choice = int(input(text))
            keylist = list(self.options)
            # Get an indexed list of keys so it can be cross referenced with the choice
            if (choice - 1) < len(keylist):
                # return self.options[keylist[choice - 1]]
                # Since the list begins at index 1 (i.e. human friendly), we subtract 1 from choice
                option = self.options[keylist[choice - 1]]
                option["fn"](option["fn_params"])
            else:
                print(colored("Incorrect choice", "red"))
                self.get_choice()
        except Exception as e:
            print(e)
            print(colored("Please input a number", color="red"))
            self.get_choice()

    def add_back_option(self, back_key, back_description, back_fn, back_fn_params):
        self.add_option(back_key, back_description, back_fn, back_fn_params)
