from typing import Callable
import logging as logger
from termcolor import colored


class menu:

    options = {}

    def add_option(self, option_id, option_text: str, option_fn: Callable = None, params = None) -> None:
        self.options[option_id] = {"option_text": option_text, "fn": option_fn, "fn_params": params}
        logger.debug("Added option: ")
        logger.debug(self.options[option_id])

    def get_options(self):
        return self.options

    def print_options(
        self,
        noback: bool = False,
        back_fn = exit,
        back_description: str = "Exit",
        back_key: str = "x",
    ):
        if not noback:
            self.add_back_option(back_key, back_description, back_fn)
        i = 1
        for option in self.options:
            print(f"{i}. {self.options[option]['option_text']}")
            i += 1

    def get_choice(self, text: str = "Enter your choice: "):
        try:
            choice = int(input(text))
            # Get an indexed list of keys so it can be cross referenced with the choice
            keylist = list(self.options)
            if (choice - 1) < len(keylist):
                # Since the list begins at index 1 (i.e. human friendly), we subtract 1 from choice
                return self.options[keylist[choice - 1]]
            else:
                print(colored("Incorrect choice", "red"))
                self.get_choice()
        except:
            print(colored("Please input a number", color="red"))
            self.get_choice()

    def add_back_option(self, back_key, back_description, back_fn):
        # self.options[back_key] = {"option_text": back_description, "fn": back_fn}
        self.add_option("return", back_description, back_fn)
