from qtpy import QtCore

class SingletonNormal(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonNormal, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonQt(type(QtCore.QObject), type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonQt, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
