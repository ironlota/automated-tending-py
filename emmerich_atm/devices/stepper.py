import time
import sys
import traceback
from typing import NoReturn
from enum import Enum

from qtpy import QtCore

from gpiozero import OutputDevice

from ..signals.finger_movement import FingerMovementSignals

class StepType(Enum):
    FULL = 'FULL'
    HALF = 'HALF'
    QUARTER = 'QUARTER'
    ONE_EIGHTH = 'ONE_EIGHTH'
    ONE_SIXTEENTH = 'ONE_SIXTEENTH'

class Stepper():
    r"""Stepper Thread Wrapper for A4988 Motor Driver

    Arguments
        sleep_pin (int) : Sleep GPIO Pin
        step_pin (int) : Step GPIO Pin
        direction_pin (int) : Direction GPIO Pin
        step_pin (int) : Step GPIO Pin
        reverse (bool, optional) : Moving backward?
        step_type (StepType, optional) : Step full, half, quarter, one_eight, or one_sixteenth
    """
    def __init__(self,
                 step_pin: int,
                 direction_pin: int,
                 step_to_cm: float,
                 step_type: StepType = StepType.FULL):
        super(Stepper, self).__init__()
        self.step = OutputDevice(step_pin)
        self.direction = OutputDevice(direction_pin)
        self.step_to_cm = step_to_cm
        self.step_type: StepType = step_type

    def set_step_type(self, step_type: StepType):
        self.step_type = step_type

    def set_direction(self, reverse: bool) -> NoReturn:
        if (reverse):
            self.direction.on()
        else:
            self.direction.off()

    def close(self) -> NoReturn:
        self.step.close()
        self.direction.close()

class StepperRunnable(QtCore.QRunnable):
    def __init__(self,
                 stepper: Stepper,
                 *args,
                 **kwargs):
        super(StepperRunnable, self).__init__()
        self.stepper = stepper
        self.args = args
        self.kwargs = kwargs
        self.signals = FingerMovementSignals()

    def move(self,
             steps: int,
             reverse: bool = False,
             step_type: StepType = StepType.FULL,
             init_delay: float = .0005,
             step_delay: float = .0005) -> NoReturn:
        r"""Forward movements.

        Arguments
            steps (int) : number of steps that stepper will do
            reverse (bool) : move backward or counterclockwise
            step_type (StepType) : type of step
            init_delay (float) : initialization delay before start moving
            step_delay (float) : delay between each step
        """

        self.stepper.set_direction(reverse)
        self.stepper.set_step_type(step_type)

        time.sleep(init_delay)

        try:
            for i in range(steps):
                self.stepper.step.off()
                time.sleep(step_delay)
                self.stepper.step.on()
                time.sleep(step_delay)
                self.signals.move.emit(i)
        except:
            exctype, value = sys.exc_info()[:2]
            traceback.print_exc()
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(steps / self.stepper.step_to_cm)
        finally:
            self.stepper.step.off()
            self.stepper.direction.off()
            self.signals.finished.emit()

    @QtCore.Slot()
    def run(self):
        self.move(*self.args, **self.kwargs)
