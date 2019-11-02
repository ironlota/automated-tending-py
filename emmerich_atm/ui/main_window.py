# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/app.ui',
# licensing of 'ui/app.ui' applies.
#
# Created: Fri Nov  1 15:59:17 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 169)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(20, 20, 181, 16))
        self.app_title.setObjectName("app_title")
        self.progressTaskBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressTaskBar.setGeometry(QtCore.QRect(90, 60, 381, 23))
        self.progressTaskBar.setProperty("value", 24)
        self.progressTaskBar.setObjectName("progressTaskBar")
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.progress_label.setObjectName("progress_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 10, 171, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.state_label = QtWidgets.QLabel(self.frame)
        self.state_label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.state_label.setObjectName("state_label")
        self.state_value = QtWidgets.QLabel(self.frame)
        self.state_value.setGeometry(QtCore.QRect(100, 10, 60, 16))
        self.state_value.setObjectName("state_value")
        self.stop_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_all_button.setGeometry(QtCore.QRect(360, 100, 113, 32))
        self.stop_all_button.setStyleSheet("#stop_all_button {\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.stop_all_button.setObjectName("stop_all_button")
        self.tending_button = QtWidgets.QPushButton(self.centralwidget)
        self.tending_button.setGeometry(QtCore.QRect(10, 100, 113, 32))
        self.tending_button.setObjectName("tending_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.app_title.setText(QtWidgets.QApplication.translate("MainWindow", "Automated Tending Machine", None, -1))
        self.progress_label.setText(QtWidgets.QApplication.translate("MainWindow", "Progress", None, -1))
        self.state_label.setText(QtWidgets.QApplication.translate("MainWindow", "State", None, -1))
        self.state_value.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.stop_all_button.setText(QtWidgets.QApplication.translate("MainWindow", "Stop All", None, -1))
        self.tending_button.setText(QtWidgets.QApplication.translate("MainWindow", "Tending", None, -1))

