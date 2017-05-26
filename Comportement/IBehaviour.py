from math import fabs
from abc import abstractmethod

class IBehaviour:

    def __init__(self):
        self.foundCan = False
    
    @abstractmethod
    def start(self): raise NotImplementedError

    @abstractmethod
    def avoidObstacle(self, IDetectable): raise NotImplementedError

    @abstractmethod
    def catchObject(self, IGrabable): raise NotImplementedError
    
    @abstractmethod
    def goTowardsCan(self, Can): raise NotImplementedError
            
    @abstractmethod
    def recheckCanPosition(self, Can): raise NotImplementedError

    @abstractmethod
    def idleLookForCan(self): raise NotImplementedError

    @abstractmethod
    def lookingForCanRoutine(self): raise NotImplementedError

    @abstractmethod
    def lookAround(self): raise NotImplementedError

    