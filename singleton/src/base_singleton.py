class BaseSingleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                BaseSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]
