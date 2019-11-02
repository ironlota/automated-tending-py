"""
State container
"""

from qtpy import QtCore

from .utils.singleton import SingletonQt

class Point(QtCore.QObject):
    x: float = 0
    y: float = 0

    def is_zero(self):
        """Check if all coordinates are zero.

        :return: boolean value.
        """
        return (self.x == 0.0 and self.y == 0)
    
"""
GPIO    = SLEEP
GPIO 23 = X STEP
GPIO 24 = X DIR
GPIO 22 = Y STEP
GPIO 25 = Y DIR
"""

class State(QtCore.QObject, metaclass=SingletonQt):
    moved = QtCore.Signal(float, float)

    def __init__(self):
        self.coordinates = Point()

    @property
    def coordinates(self) -> Point:
        return self.coordinates

    @property
    def x(self) -> float:
        return self.coordinates.x

    @property
    def y(self) -> float:
        return self.coordinates.y

    @x.setter
    def x(self, new_x: float):
        self.coordinates.x = new_x
        # After the center is moved, emit the moved
        # signal with the new coordinates
        self.moved.emit(new_x, self.y)

    @y.setter
    def y(self, new_y: float):
        self.coordinates.y = new_y
        # After the center is moved, emit the moved
        # signal with the new coordinates
        self.moved.emit(self.x, new_y)
