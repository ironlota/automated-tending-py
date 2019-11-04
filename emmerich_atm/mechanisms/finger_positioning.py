from typing import NoReturn

from qtpy import QtCore

from gpiozero import OutputDevice

from ..config import Config
from ..state import State

from ..devices.stepper import Stepper, StepperThread, StepperRunnable

class FingerPositioning(QtCore.QThread):
    def __init__(self):
        super(FingerPositioning, self).__init__()
        self.config = Config().config['finger']['positioning']
        self.sleep = OutputDevice(self.config['sleep_pin'], active_high=False)

        self.mutex_x = QtCore.QMutex()
        self.mutex_y = QtCore.QMutex()

        self.state = State()

        self.stepper_x = Stepper(
            step_pin=self.config['x']['step_pin'],
            direction_pin=self.config['x']['direction_pin'],
            step_to_cm=self.config['x']['step_to_cm'])

        self.stepper_y = Stepper(
            step_pin=self.config['y']['step_pin'],
            direction_pin=self.config['y']['direction_pin'],
            step_to_cm=self.config['y']['step_to_cm'])

        
        # self.stepper_x_worker = StepperThread(stepper=self.stepper_x,
        #                                        parent=self,
        #                                        steps=100,
        #                                        reverse=True)

        self.stepper_x_worker = StepperRunnable(
            stepper=self.stepper_x,
            steps=1000,
            reverse=True)
        self.stepper_x_worker.moveToThread(self)
        self.stepper_x_worker.signals.move.connect(self.log_step_x)
        self.stepper_x_worker.signals.result.connect(self.update_state_x)
        self.stepper_x_worker.signals.finished.connect(self.finish)

        # self.stepper_y_worker = StepperThread(stepper=self.stepper_y,
        #                                       parent=self,
        #                                       steps=100,
        #                                       reverse=True)
        self.stepper_y_worker = StepperRunnable(
            stepper=self.stepper_y,
            steps=1000,
            reverse=True)
        self.stepper_y_worker.signals.moveToThread(self)
        self.stepper_y_worker.signals.move.connect(self.log_step_y)
        self.stepper_y_worker.signals.result.connect(self.update_state_y)
        self.stepper_y_worker.signals.finished.connect(self.finish)
        
        self.threadpool = QtCore.QThreadPool()

        self.sleep.off()

    def __del__(self):
        self.wait()
        self.threadpool.clear()
        self.sleep.close()
        self.stepper_x.close()
        self.stepper_y.close()

    @QtCore.Slot(int)
    def log_step_x(self, x: int):
        print('Stepping x in {} steps'.format(x))

    @QtCore.Slot(int)
    def log_step_y(self, y: int):
        print('Stepping y in {} steps'.format(y))

    @QtCore.Slot(float)
    def update_state_x(self, x: float):
        self.mutex_x.lock()
        self.state.x += x
        self.mutex_x.unlock()

    @QtCore.Slot()
    def update_state_y(self, y: float):
        self.mutex_y.lock()
        self.state.y += y
        self.mutex_y.unlock()

    @QtCore.Slot()
    def finish(self):
        self.sleep.on()

    @QtCore.Slot()
    def run(self):
        # stepper_x_worker = StepperRunnable(stepper=self.stepper_x,
        #                                    steps=1000,
        #                                    reverse=True)
        # stepper_x_worker.signals.moveToThread(self)
        # stepper_x_worker.signals.move.connect(self.log_step_x)
        # stepper_x_worker.signals.result.connect(self.update_state_x)
        # stepper_x_worker.signals.finished.connect(self.finish)
        
        # stepper_y_worker = StepperThread(stepper=self.stepper_y,
        #                                  parent=self,
        #                                  steps=100,
        #                                  reverse=True)
        # stepper_y_worker.signals.move.connect(self.log_step_y)
        # stepper_y_worker.signals.result.connect(self.update_state_y)
        # stepper_y_worker.signals.finished.connect(self.finish)

        # self.stepper_x_worker.start()
        # self.stepper_y_worker.start()
        # stepper_y_worker.wait()
        # stepper_x_worker.wait()
        
        self.threadpool.start(self.stepper_x_worker)
        self.threadpool.start(self.stepper_y_worker)
        self.threadpool.waitForDone()
