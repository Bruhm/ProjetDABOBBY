#include "i2c.h"
#include "pilotage.h"


int pin_sharp = A0;  // fil jaune du capteur sharp branché a A0

// the setup routine runs once when you press reset:
void setup() {
    // initialize the digital pin as an output.
    INIT_I2C();
    INIT_MOTORS_PINS();
    Serial.begin(9600);  // initialisation communication série
    analogReference(EXTERNAL); // tension analogique max sera 3,3 V
                             // si AREF est relié  3,3 V  


     digitalWrite(M11, HIGH);
      analogWrite(go2, 255);
      delay(20000);
    
   
}

// the loop routine runs over and over again forever:
void loop() {

  
}

