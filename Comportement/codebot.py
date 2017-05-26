####################################################################
# This is a stubbed bot implementing the IBehaviour interface      #
# Its only purpose is for code testing in a simulated environment  #
# where the bot knows its position and angle and has knowledge of  #
# every can position                                               #
####################################################################

from IBehaviour import IBehaviour
from random import randint
from time import sleep

import math

class CodeBot: 

    MIN_SURFACE_TO_GRAB_OBJECT = 10000
    ANGLE_TOLERANCE = 5
    TURNING_ANGLE_STEP = 5
    SURFACE_FOR_MINIMAL_CAN_DETECTION = 500

    def __init__(self):
        self.cansInEnvironement = []
        self.foundCan = False
        self.lockedCan = None
        self.posX = 0
        self.posY = 0
        self.angle = 0
    
    # For now, bot starts by idling and looking for cans
    def start(self):
        while True:
            print('Bot is starting !')
            sleep(1.5)
            print('Randomizing bot starting angle')
            self.angle = randint(0, 359)
            sleep(1.5)
            print('Bot is now looking for cans ...')
            self.idleLookForCan()
            sleep(1.5)
            self.goTowardsCan(self.lockedCan)
            sleep(1.5)
            print(self.catchObject(self.lockedCan))
            sleep(1.5)
            print('Bot is back to idling\n')
            self.lockedCan.angle = randint(0,359) # Resetting locked can position
            self.lockedCan = None
            self.foundCan = False
            sleep(1.5)

    def avoidObstacle(self, IDetectable):
        if IDetectable.angle >= 0:
            return 'Dodge Droit'
        else:
            return 'Dodge Gauche'

    def catchObject(self, IGrabable):
        if IGrabable.isGrabable and IGrabable.surface >= self.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object grabed'
        elif IGrabable.isGrabable and IGrabable.surface < self.MIN_SURFACE_TO_GRAB_OBJECT:
            return 'Object is too far to be grabed' 
        else:
            return 'Object can\'t be grabed'
    
    def goTowardsCan(self, Can):
       while Can.surface < self.MIN_SURFACE_TO_GRAB_OBJECT:
            Can.surface += 1000 # Go towards the can

    def idleLookForCan(self):
        while not self.foundCan:
            self.lookingForCanRoutine()

    def lookingForCanRoutine(self):
        self.lookAround()

    def lookAround(self):
        turnedDegrees = 0
        while not self.foundCan and turnedDegrees < 360:
            sleep(0.05)
            self.findClosestCan()
            if not self.foundCan:
                self.turnRight(self.TURNING_ANGLE_STEP)
                turnedDegrees += self.TURNING_ANGLE_STEP
        if turnedDegrees >= 360:
            print("Bot did a full turn without finding a can")
    
    def turnRight(self, angle):
        self.angle = (self.angle + angle) % 360

    # This function is a stub of the camera detection by the robot which is
    # supposed to return the surface of a detected cam.
    #
    # Instead of a surface threshold to activate movement, we will in this case 
    # use the angle and distance values of the bot
    def findClosestCan(self):
        for can in self.cansInEnvironement:
            if math.fabs(can.angle - self.angle) < self.ANGLE_TOLERANCE and can.surface > self.SURFACE_FOR_MINIMAL_CAN_DETECTION:
                self.lockedCan = can
                self.foundCan = True
                print('Locked can with values - angle : ' + str(can.angle) + ' surface : ' +  str(can.surface) )
            else:
                can.surface = randint(400,1000) # randomize a new surface value for test purposes


