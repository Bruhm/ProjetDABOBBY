#include "i2c.h"

int dataReceived = 0;
int resolution = 100;
int uptime = 0;
int function_id = 0;

void INIT_I2C() {
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(receiveData);
    Wire.onRequest(dataCheck);
}

void receiveData(int byteCount){
    while(Wire.available()) {
        dataReceived = Wire.read();

        uptime = (dataReceived & 0xF);
        function_id = ((dataReceived >> 4) & 0xF);
        switch (function_id)
        {
          case 1:
            ALL_MOTORS_ON();
          break;
          case 2:
            ALL_MOTORS_OFF();
          break;
          case 3:
            TURN_LEFT();
          break;
          case 4:
            TURN_RIGHT();
          break;
          case 5:
            SET_MOTORS_FORWARDS();
          break;
          case 6:
            SET_MOTORS_BACKWARDS();
          break;
          case 7:
            UNSET_MOTORS();
          break;
          default:
            Serial.print("Function out of range");
          break;
        }
    }
}



void dataCheck(){
    Wire.write( function_id );
}

