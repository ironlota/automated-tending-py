import pytest

import os

from emmerich_atm.config import Config

from .utils.mock_signal import MockSignal
from .utils.mock_config import config_str

class TestConfig:
    @pytest.fixture(autouse=True)
    def setup_method(self, tmpdir):
        self.yaml = tmpdir.mkdir('config').join('config.yaml')
        self.yaml.write(config_str)
        self.config = Config(filename=self.yaml).config
    
    def test_singleton(self):
        config = Config(filename=self.yaml).config
        assert self.config == config

    def test_value(self):
        assert self.config['finger']['positioning']['sleep_pin'] == 16
