from IDetectable import IDetectable

class IGrabable:
    def __init__(self, surface=0, angle=0):
        IDetectable.__init__(self, surface, angle)
        self.isGrabable = True
        