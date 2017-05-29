from IDetectable import IDetectable

class IGrabable:
    def __init__(self, surface=0, angle=0):
        self.IDetectable = IDetectable(surface, angle)
        self.isGrabableVar = True
    def isGrabable(self):
        return self.isGrabableVar

        