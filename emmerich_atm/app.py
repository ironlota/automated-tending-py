"""
Automated Tending Machine
"""

import sys
from qtpy import QtWidgets

class EmmerichAutomatedTendingApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Emmerich Automated Tending')
        self.show()

        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = EmmerichAutomatedTendingApp()
    sys.exit(app.exec_())
