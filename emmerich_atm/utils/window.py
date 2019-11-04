"""
Wrapper for QT Window
"""

from qtpy import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):
    def __init__(self, ui: object):
        super(Window, self).__init__()
        self.init_ui(ui)

    def init_ui(self, ui: object) -> None:
        self.ui = ui()
        self.ui.setupUi(self)
