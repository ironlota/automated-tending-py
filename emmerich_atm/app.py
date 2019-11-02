"""
Automated Tending Machine
"""
 
import sys
from qtpy import QtCore, QtWidgets

from .utils.window import Window

from .ui.main_window import Ui_MainWindow

from .state import State
from .mechanisms.finger_positioning import FingerPositioning

class EmmerichAutomatedTendingApp(Window):
    def __init__(self):
        super(EmmerichAutomatedTendingApp, self).__init__(Ui_MainWindow)
        self.show()
        self.threadpool = QtCore.QThreadPool()
        self.tending_button.connect(self.init_finger_movement)

    def init_finger_movement(self):
        self.threadpool.start(FingerPositioning())
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = EmmerichAutomatedTendingApp()
    # main_window.init_device()
    sys.exit(app.exec_())
