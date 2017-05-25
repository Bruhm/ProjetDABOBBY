class Behaviour:

    MIN_SURFACE_TO_GRAB_OBJECT = 10000

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

