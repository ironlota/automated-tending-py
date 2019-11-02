"""
State container
"""

from .utils.singleton import Singleton

class Point:
    x = 0
    y = 0

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

class State(metaclass=Singleton):
    coordinates = Point()
