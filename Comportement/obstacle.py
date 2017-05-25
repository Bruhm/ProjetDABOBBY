from IDetectable import IDetectable

class Obstacle(IDetectable):
    def __init__(self, surface = 0, angle = 0):
        IDetectable.__init__(self, surface, angle)