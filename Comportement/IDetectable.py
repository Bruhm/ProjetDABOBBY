# IDetectable is the interface used to define the detected object by the camera.
# Surface is the surface of the detected object in pixels.
# Angle is the angle of the position of the object relative to the bot direction.
# Angle will be a negative value if the object is on the left of the bot, positive otherwise.

class IDetectable:
    def __init__(self, surface=0, angle=0):
        self.surface = surface
        self.angle = angle
        self.isGrabable = False
