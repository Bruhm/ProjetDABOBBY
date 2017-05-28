import threading

from IBehaviour import IBehaviour
from Detection.camera import Camera, RedObserver
from RaspberryICC.ICCConnexion import ICCArduino, Functions

class CanBot:

    MIN_SURFACE_TO_GRAB_OBJECT = 40000
    MUTEX_VIDEO = threading.Event()

    def __init__(self):
        self.camera = Camera()
        self.redObserver = RedObserver()
        self.iccBus = ICCArduino()
        self.lockedCan = None
        self.hasCan = False

        
    def start(self):
        ## Initiating Camera ##
        self.camera.register(self.redObserver)
        threadCamera = threading.Thread(target=self.camera.threadScanVideo, args=([self.MUTEX_VIDEO]))

    def avoidObstacle(self, IDetectable):
        raise NotImplementedError

    def catchObject(self, IGrabable):
        if self.canCatchObject(IGrabable):
            self.iccBus.sendFunctionToArduino(Functions.MAGNET_ON , 0)
            self.iccBus.sendFunctionToArduino(Functions.SET_MOTORS_FORWARDS , 0)
            self.iccBus.sendFunctionToArduino(Functions.ALL_MOTORS_ON , 0)


    def canCatchObject(self, IGrabable):
        if IGrabable.isGrabable and IGrabable.surface >= self.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object grabed'
        elif IGrabable.isGrabable and IGrabable.surface < self.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object is too far to be grabed'
        else:
            return 'Object can\'t be grabed'

    def goTowardsCan(self, Can):
        raise NotImplementedError

    def recheckCanPosition(self, Can):
        raise NotImplementedError

    def idleLookForCan(self):
        raise NotImplementedError

    def lookingForCanRoutine(self):
        raise NotImplementedError

    def lookAround(self):
        raise NotImplementedError