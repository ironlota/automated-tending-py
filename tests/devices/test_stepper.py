import pytest
from unittest import mock

from qtpy import QtCore

from emmerich_atm.devices.stepper import StepperThread

from ..utils.mock_signal import MockSignal

class TestStepper:
    @mock.patch('emmerich_atm.devices.stepper.Stepper', autospec=True)
    def setup_method(self, _, MockStepper):
        self.stepper = MockStepper(step_pin=1, direction_pin=2, step_to_cm=3)

    def test_step(self):
        self.stepper.set_direction(False)
        self.stepper.set_direction.assert_called()

    def test_close(self):
        self.stepper.close()
        self.stepper.close.assert_called()
        
class TestStepperThread:
    class Callback:
        count_move_cb = 0
        count_result_cb = 0
        count_finished_cb = 0

        @QtCore.Slot()
        def move_callback(self, _: int):
            self.count_move_cb += 1

        @QtCore.Slot()
        def result_callback(self, _: float):
            self.count_result_cb += 1

        @QtCore.Slot()
        def finished_callback(self):
            self.count_finished_cb += 1

    @mock.patch('emmerich_atm.devices.stepper.Stepper', autospec=True)
    @mock.patch('gpiozero.OutputDevice', autospec=True)
    def setup_method(self, _, mock_output_device, mock_stepper):
        self.stepper = mock_stepper.return_value
        self.stepper.step_to_cm = 12
        self.stepper.step = mock_output_device.return_value
        self.stepper.direction = mock_output_device.return_value

        self.stepper_thread = StepperThread(stepper=self.stepper,
                                            steps=100,
                                            reverse=True)

        
        self.callback = TestStepperThread.Callback()

        self.stepper_thread.signals.move.connect(self.callback.move_callback)
        self.stepper_thread.signals.result.connect(self.callback.result_callback)
        self.stepper_thread.signals.finished.connect(self.callback.finished_callback)

    def teardown_method(self):
        pass

    def test_move(self, qtbot):
        with qtbot.waitSignal(self.stepper_thread.finished):
            # blocker.connect(self.stepper_thread.signals.move)
            self.stepper_thread.start()

        assert self.callback.count_move_cb == 100
        assert self.callback.count_result_cb == 1
        assert self.callback.count_finished_cb == 1
        self.stepper.set_direction.assert_called()
        self.stepper.step.on.assert_called()
