from typing import NoReturn

from qtpy import QtCore

from gpiozero import OutputDevice

from ..config import Config
from ..state import State

from ..devices.stepper import Stepper, StepperRunnable

class FingerPositioning(QtCore.QRunnable):
    def __init__(self):
        super(FingerPositioning, self).__init__()
        self.config = Config().get_config()['finger']['positioning']
        self.sleep = OutputDevice(self.config['sleep_pin'], active_high=False)

        self.mutex = QtCore.QMutex()
        
        self.stepper_x = Stepper(
            step_pin=self.config['x']['step_pin'],
            direction_pin=self.config['x']['direction_pin'])
        
        self.stepper_x.signals.move.connect(self.log_step_x)
        self.stepper_x.signals.result.connect(self.update_state_x)
        
        self.stepper_y = Stepper(
            step_pin=self.config['y']['step_pin'],
            direction_pin=self.config['y']['direction_pin'])

        self.stepper_y.signals.move.connect(self.log_step_y)
        self.stepper_y.signals.result.connect(self.update_state_y)

        self.threadpool = QtCore.QThreadPool()

    def __del__(self):
        self.sleep.close()
        self.stepper_x.close()
        self.stepper_y.close()

    def log_step_x(self, x: int):
        print('Stepping x in {} steps'.format(x))

    def log_step_y(self, y: int):
        print('Stepping y in {} steps'.format(y))
        
    def update_state_x(self, x: float):
        self.mutex.lock()
        State.coordinates.x += x
        self.mutex.unlock()

    def update_state_y(self, y: float):
        self.mutex.lock()
        State.coordinates.y += y
        self.mutex.unlock()
        
    def run(self):
        # x: int,
        # y: int,
        # init_delay: float = .0005,
        # step_delay: float = .0005) -> NoReturn:
        stepper_x_worker = StepperRunnable(self.stepper_x,
                                           steps=100,
                                           reverse=True)
        self.threadpool.start(stepper_x_worker)
        # self.stepper_x.forward(x / 100, init_delay)
        # self.stepper_y.forward(y / 100)
