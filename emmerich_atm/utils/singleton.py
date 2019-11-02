from qtpy import QtCore

class SingletonNormal(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonQt(QtCore.pyqtWrapperType, type):
    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        cls.instance = None
    
    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kw)
        return cls.instance
