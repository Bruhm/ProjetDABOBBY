class Subject(object):
    """Observer pattern http://en.wikipedia.org/wiki/Observer_pattern
    """
    def __init__(self, *args, **kwargs):
        pass

    def register(self, observer):
        pass

    def unregister(self, observer):
        pass

    def notify_all(self, *args, **kwargs):
        pass

class Observer(object):
    def __init__(self, *args, **kwargs):
        pass

    def notify(self, *args, **kwargs):
        pass


