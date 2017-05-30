#include "i2c.h"
#include "pilotage.h"

int count = 0;
// the setup routine runs once when you press reset:
void setup() {
    // initialize the digital pin as an output.
    INIT_MAGNET();
    INIT_MOTORS_PINS();
    INIT_I2C();
    Serial.begin(9600);  // initialisation communication série
    analogReference(EXTERNAL); // tension analogique max sera 3,3 V
                             // si AREF est relié  3,3 V 
    
}

// the loop routine runs over and over again forever:
void loop() {
  distance = 32076.69016894*pow(valeur_moyenne(10), -1.245865753);
  if ( distance < 10 )
        {
          ObstacleFound = true;
          ALL_MOTORS_ON();
          SET_MOTORS_BACKWARDS();
          delay(200);
          if( count == 3 )
          {
            count = 0;
           TURN_LEFT();
           }
           else
           {
            count = count +1;
            TURN_RIGHT();
           }
          delay(200);
          ALL_MOTORS_OFF();
        }
  else
        {
          ObstacleFound = false;
        }
   Serial.println(distance);
}

