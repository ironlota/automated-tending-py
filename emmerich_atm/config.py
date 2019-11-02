import yaml

from .utils.singleton import Singleton

class Config(metaclass=Singleton):
    def __init__(self):
        with open("config.yaml", 'r') as ymlfile:
            self.cfg = yaml.safe_load(ymlfile)

    def get_config(self):
        return self.cfg
