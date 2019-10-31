"""
Automated Tending Machine
"""

import sys
from qtpy import QtWidgets

from .state import State

from .stepper import Stepper

class EmmerichAutomatedTendingApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.stepper_x = Stepper(step_pin=23, direction_pin=24)
        self.stepper_y = Stepper(step_pin=22, direction_pin=25)

    def init_ui(self):
        self.setWindowTitle('Emmerich Automated Tending')
        self.show()

    def init_device(self):
        self.stepper_x.forward(200)
        self.stepper_y.forward(300)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = EmmerichAutomatedTendingApp()
    sys.exit(app.exec_())
