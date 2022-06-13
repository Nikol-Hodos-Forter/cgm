import yaml
import logging

class Config:
    
    config_file = "config.yaml"
    config = {}
    _instance = None
    
    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.debug(f"Loaded configuration from {self.config_file}")
        with open(self.config_file) as y:
            self.config = yaml.full_load(y.read())
            
    def get_config(self):
        return self.config