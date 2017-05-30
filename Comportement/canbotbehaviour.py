import threading
import time
from IBehaviour import IBehaviour
from camera import Camera, ObjectObserver
from ICCConnexion import ICCArduino, Functions

class CanBot:
    TIME_REACTION = 0.1
    X_FORWARD = 50
    MIN_SURFACE_TO_GRAB_OBJECT = 30000
    MUTEX_VIDEO = threading.Event()
    NOT_FOUND = -1159

    def __init__(self):
        self.camera = Camera()
        self.canObserver = ObjectObserver(True)
        self.baseObserver = ObjectObserver(False)
        #self.limiteObserver = ObjectObserver(False)
        self.observerObject = self.canObserver
        self.iccBus = ICCArduino()
        self.lockedCan = None
        self.hasCan = False
        self.timer = 3
        
    def start(self):
        ## Initiating Camera ##
        self.camera.register(self.canObserver)
        self.camera.register(self.baseObserver)
        #self.camera.register(self.limiteObserver)
        threadCamera = threading.Thread(target=self.camera.threadScanVideo, args=([self.MUTEX_VIDEO]))
        try:
            threadCamera.start()
            self.iccBus.sendFunctionToArduino(Functions.INITIALISATION , 0)
            while(True):
                time.sleep(1)
                self.lookAround()
                
            while not halt:
                continue
            print("[HALT] Main thread")

        except Exception as ex:
                self.iccBus.sendFunctionToArduino(Functions.ALL_MOTORS_OFF , 0)
                print(ex)

    def avoidObstacle(self, IDetectable):
        raise NotImplementedError

    def catchObject(self):
        self.iccBus.sendFunctionToArduino(Functions.MAGNET_ON , 0)
        time.sleep(0.5)
        self.iccBus.sendFunctionToArduino(Functions.SERVO_ON , 0)

    def releaseObject(self):
        self.iccBus.sendFunctionToArduino(Functions.MAGNET_OFF , 0)
        time.sleep(0.5)
        self.iccBus.sendFunctionToArduino(Functions.SERVO_OFF , 0)
        
    def canCatchObject(self, IGrabable):
        if IGrabable.isGrabable and IGrabable.surface >= self.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object grabed'
        elif IGrabable.isGrabable and IGrabable.surface < self.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object is too far to be grabed'
        else:
            return 'Object can\'t be grabed'

    def goTowardsCan(self,can):
        while(can.isLooked and not self.hasCan):
            if can.surface > self.MIN_SURFACE_TO_GRAB_OBJECT:
                if can.isGrabable:
                    print "grab"
                    self.catchObject()
                    self.observerObject = self.baseObserver
                    break
                else:
                    print "release"
                    self.releaseObject()
                    self.observerObject = self.canObserver
                break
            else:
                self.robotGo(can.X())
                
    
    def robotGo(self,X):
        self.iccBus.sendFunctionToArduino(Functions.ALL_MOTORS_ON , 0)
        if(X < self.X_FORWARD and X > -self.X_FORWARD):
            print "go forward"
            print X
            self.iccBus.sendFunctionToArduino(Functions.SET_MOTORS_FORWARDS , 0)
            time.sleep(self.TIME_REACTION)
        elif(X < 0 and X != self.NOT_FOUND):
            print "turn right"
            self.iccBus.sendFunctionToArduino(Functions.TURN_RIGHT , 0)
            time.sleep(self.TIME_REACTION)
        elif(X > 0 and X != self.NOT_FOUND):
            print "turn left"
            self.iccBus.sendFunctionToArduino(Functions.TURN_LEFT , 0)
            time.sleep(self.TIME_REACTION)
        else:
            self.iccBus.sendFunctionToArduino(Functions.ALL_MOTORS_OFF , 0)
            time.sleep(self.TIME_REACTION)
            print "ya rien"
            self.observerObject.isLooked = False
            pass
            
    
    def recheckCanPosition(self, Can):
        raise NotImplementedError

    def idleLookForCan(self):
        raise NotImplementedError

    def lookingForCanRoutine(self):
        raise NotImplementedError
    
    #function recherche can
    def lookAround(self):
        self.CheackObject()
        count = 0
        while(not self.observerObject.isLooked):
            time.sleep(1)
            count = count +1
            if(count == 2):
                print "recherche"
                self.iccBus.sendFunctionToArduino(Functions.ALL_MOTORS_ON , 0)
                self.iccBus.sendFunctionToArduino(Functions.TURN_RIGHT , 0)
                time.sleep(0.2)
                self.iccBus.sendFunctionToArduino(Functions.SET_MOTORS_FORWARDS , 0)
                time.sleep(0.2)
                self.iccBus.sendFunctionToArduino(Functions.ALL_MOTORS_OFF , 0)
                count = 0
            self.CheackObject()
                
    
    def CheackObject(self):
        count = 0
        print self.observerObject.X()
        if self.observerObject.X() != self.NOT_FOUND and self.observerObject.Surface() != self.NOT_FOUND :
            self.observerObject.isLooked = True
            self.goTowardsCan(self.observerObject)
        else:
            print "rien"
            self.observerObject.isLooked = False

        

            

            
        
        
    
