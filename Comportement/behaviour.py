from math import fabs

class Behaviour:

    MIN_SURFACE_TO_GRAB_OBJECT = 10000
    ANGLE_TOLERANCE = 5

    def __init__(self):
        pass
        
    def avoidObstacle(self, IDetectable):
        if IDetectable.angle >= 0:
            return 'Dodge Droit'
        else:
            return 'Dodge Gauche'

    def catchObject(self, IGrabable):
        if IGrabable.isGrabable and IGrabable.surface >= Behaviour.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object grabed'
        elif IGrabable.isGrabable and IGrabable.surface < Behaviour.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object is too far to be grabed' 
        else:
            return 'Object can\'t be grabed'
    
    def goTowardsCan(self, Can):
        while fabs(Can.angle) > Behaviour.ANGLE_TOLERANCE and Can.surface < Behaviour.MIN_SURFACE_TO_GRAB_OBJECT:
            # function to recheck can position
            self.recheckCanPosition(Can)
            

    # This is a stub function of the cam recheck for a can
    def recheckCanPosition(self, Can): 
        if Can.angle > 0:
            Can.angle -= 1 # Go left
        else:
            Can.angle += 1 # Go right

        if Can.surface < Behaviour.MIN_SURFACE_TO_GRAB_OBJECT:
            Can.surface += 1000 # Go towards the can

  #  def idleLookForCan(self):
