import pytest

from emmerich_atm.state import State

from .utils.mock_signal import MockSignal

class TestState:
    def setup_method(self):
        self.state = State()
        self.handler = MockSignal()
        self.state.moved.connect(self.handler.movedSignalReceived)

    def teardown_method(self):
        self.handler.reset_counter()
        self.state.reset_coordinates()

    def test_singleton(self):
        state_ = State()
        assert self.state == state_

    def test_add_x(self, qtbot):
        with qtbot.waitSignal(self.state.moved, raising=False):
            self.state.x = 2.0

        assert self.state.x == 2.0
        assert self.handler.call_count == 1

    def test_add_y(self, qtbot):
        with qtbot.waitSignal(self.state.moved, raising=False):
            self.state.y += 2.0

        assert self.state.y == 2.0
        assert self.handler.call_count == 1
