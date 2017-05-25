from IGrabable import IGrabable

class Can:
    def __init__(self, surface = 0, angle = 0):
        IGrabable.__init__(self,surface,angle)
        self.angle = angle