import time
import sys
from typing import NoReturn

from enum import Enum

from gpiozero import OutputDevice

class StepType(Enum):
    FULL = 'FULL'
    HALF = 'HALF'
    QUARTER = 'QUARTER'
    ONE_EIGHTH = 'ONE_EIGHTH'
    ONE_SIXTEENTH = 'ONE_SIXTEENTH'

class StepperConfiguration:
    """StepperConfiguration factory
    """
    # enable: int = 0
    sleep: int = 0
    step: int = 0
    direction: int = 0
    step_type: StepType = StepType.FULL
    reverse: bool = False

class Stepper():
    r"""Stepper Wrapper for A4988 Motor Driver

    Arguments
        sleep_pin (int) : Sleep GPIO Pin
        step_pin (int) : Step GPIO Pin
        direction_pin (int) : Direction GPIO Pin
        step_pin (int) : Step GPIO Pin
        reverse (bool, optional) : Moving backward?
        step_type (StepType, optional) : Step full, half, quarter, one_eight, or one_sixteenth
    """
    def __init__(self,
                 sleep_pin: int,
                 step_pin: int,
                 direction_pin: int,
                 reverse: bool = False,
                 step_type: StepType = StepType.FULL):
        # self.enable = OutputDevice(config.enable)
        # self.sleep = OutputDevice(sleep_pin, initial_value=True)
        self.step = OutputDevice(step_pin)
        self.direction = OutputDevice(direction_pin, initial_value=reverse)
        self.step_type: StepType = step_type

    def set_step_type(self, step_type: StepType):
        self.step_type = step_type

    def set_direction(self, reverse: bool):
        if (reverse):
            self.direction.off()
        else:
            self.direction.on()
        
    def forward(self,
                steps: int,
                reverse: bool = False,
                step_type: StepType = StepType.FULL,
                init_delay: float = .05,
                step_delay: float = .005) -> NoReturn:
        r"""Forward movements.

        Arguments
            steps (int) : number of steps that stepper will do
            reverse (bool) : move backward or counterclockwise
            step_type (StepType) : type of step
            init_delay (float) : initialization delay before start moving
            step_delay (float) : delay between each step
        """

        # self.sleep.off()
        self.set_direction(reverse)
        self.set_step_type(step_type)

        time.sleep(init_delay)

        try:
            for _ in range(steps):
                self.step.off()
                time.sleep(step_delay)
                self.step.on()
                time.sleep(step_delay)
        except KeyboardInterrupt:
            print("User Keyboard Interrupt")
        except Exception as stepper_error:
            print(sys.exc_info()[0])
            print(stepper_error)
        finally:
            # self.sleep.off()
            self.step.off()
            self.direction.off()
