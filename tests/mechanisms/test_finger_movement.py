import pytest
from unittest import mock

import qtpy

from emmerich_atm.mechanisms.finger_positioning import FingerPositioning
from emmerich_atm.config import Config

from ..utils.mock_config import config_str

class TestFingerPositioning:
    @pytest.fixture(autouse=True)
    def setup_method(self, tmpdir):
        self.yaml = tmpdir.mkdir('config').join('config.yaml')
        self.yaml.write(config_str)
        self.config = Config(filename=self.yaml).config
        
        with mock.patch('emmerich_atm.mechanisms.finger_positioning.FingerPositioning.__init__', mock.Mock(return_value=None)):
            self.finger_positioning = FingerPositioning()
            self.finger_positioning.config = self.config
            with mock.patch('gpiozero.OutputDevice', autospec=True) as mock_output_device:
                self.finger_positioning.sleep = mock_output_device.return_value
        
    def teardown_method(self):
        pass

    def test_w(self, qtbot):
        pass
