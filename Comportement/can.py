from IGrabable import IGrabable

class Can:
    
    def __init__(self, surface=0, angle=0):
        self.IGrabable = IGrabable(surface, angle)
        self.angle = angle
        self.surface = surface