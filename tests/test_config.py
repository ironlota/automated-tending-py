import pytest

import os

from emmerich_atm.config import Config

from .utils.mock_signal import MockSignal

yaml_str = """
finger:
  positioning:
    sleep_pin: 16
    x:
      step_pin: 20
      direction_pin: 21
      step_to_cm: 0.5
    y:
      step_pin: 6
      direction_pin: 26
      step_to_cm: 0.3
    limit_switch: 19
"""

class TestConfig:
    @pytest.fixture(autouse=True)
    def setup_method(self, tmpdir):
        self.yaml = tmpdir.mkdir('config').join('config.yaml')
        self.yaml.write(yaml_str)
        self.config = Config(filename=self.yaml).config

    def teardown_method(self, tmpdir):
        pass
    
    def test_singleton(self):
        config = Config(filename=self.yaml).config
        assert self.config == config

    def test_value(self):
        assert self.config['finger']['positioning']['sleep_pin'] == 16
