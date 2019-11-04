import yaml

from .utils.singleton import SingletonQt

class Config(metaclass=SingletonQt):
    def __init__(self, filename='config.yaml'):
        with open(filename, 'r') as ymlfile:
            self._cfg = yaml.safe_load(ymlfile)

    @property
    def config(self):
        return self._cfg
