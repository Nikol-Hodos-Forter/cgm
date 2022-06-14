import logging

import yaml


class Config(object):
    CONFIG_FILE = "config.yaml"
    config = {}
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logging.debug("Reading config")
            cls._instance = super(Config, cls).__new__(cls)

            logger = logging.getLogger(__name__)
            logger.debug(f"Loaded configuration from {Config.CONFIG_FILE}")
            with open(Config.CONFIG_FILE) as y:
                cls.config = yaml.full_load(y.read())

        return cls._instance

    def get_config(self):
        return self.config
