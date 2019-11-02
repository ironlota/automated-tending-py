from qtpy import QtCore

class FingerMovementSignals(QtCore.QObject):
    # moveX = QtCore.Signal(int)
    # moveY = QtCore.Signal(int)
    finished = QtCore.Signal()  # QtCore.Signal
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(float)
    move = QtCore.Signal(int)
