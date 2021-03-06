import smbus
import time
from enum import Enum

class Functions(Enum):
    ALL_MOTORS_ON=1
    ALL_MOTORS_OFF=2
    TURN_LEFT=3
    TURN_RIGHT=4 
    SET_MOTORS_FORWARDS=5 
    SET_MOTORS_BACKWARDS=6 
    UNSET_MOTORS=7
    MAGNET_OFF=8
    MAGNET_ON=9
    
    # This function will form a byte composed with 2 parts : the function id, and the number of steps we want the function running
    #                         x x x x               x x x x
    #                  function_id (0 - 15)       time (0 - 15)
    # The time will be multiplied at runtime by a fixed polling rate on the arduino

class ICCArduino:
    def sendFunctionToArduino(self, function_id, time):
        # Replace 0 with 1 if a new Raspberry is used
        bus = smbus.SMBus(1)
        address = 0x12
        byteToSend = (function_id << 4) + time
        bus.write_byte(address, byteToSend)

        reponse = bus.read_byte(address)
        print("Reponse : ", reponse)

