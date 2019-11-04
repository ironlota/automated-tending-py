"""
State container
"""

from qtpy import QtCore

from typing import NoReturn

from .utils.singleton import SingletonQt

class Point(QtCore.QObject):
    x: float = 0
    y: float = 0

    def is_zero(self):
        """Check if all coordinates are zero.

        :return: boolean value.
        """
        return (self.x == 0.0 and self.y == 0)
    
class State(QtCore.QObject, metaclass=SingletonQt):
    ## States
    _coordinates = Point()

    ## Signals
    moved = QtCore.Signal(float, float)

    ## Public methods
    def reset_coordinates(self):
        self._coordinates = Point()

    ## Private methods
    def _get_coordinates(self) -> Point:
        return self._coordinates

    def _set_coordinates(self, coordinates: Point) -> Point:
        self._coordinates = coordinates
        self.moved.emit(coordinates.x, coordinates.y)

    def _get_x(self) -> float:
        return self._coordinates.x

    def _set_x(self, new_x: float) -> NoReturn:
        self._coordinates.x = new_x
        self.moved.emit(new_x, self.y)
    
    def _get_y(self) -> float:
        return self._coordinates.y

    def _set_y(self, new_y: float) -> NoReturn:
        self.coordinates.y = new_y
        self.moved.emit(self.x, new_y)

    ## Custom Properties
    coordinates = property(_get_coordinates, _set_coordinates)
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    
