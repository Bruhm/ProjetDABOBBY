#include "pilotage.h"

void INIT_MOTORS_PINS()
{
    pinMode(M11, OUTPUT);
    pinMode(M12, OUTPUT);
    pinMode(M21, OUTPUT);
    pinMode(M22, OUTPUT);
}

void ALL_MOTORS_ON()
{
    SET_MOTORS_FORWARDS();
    analogWrite(go, 255);
    analogWrite(go2, 255);
}

void ALL_MOTORS_OFF()
{
    UNSET_MOTORS();
    analogWrite(go, 0);
    analogWrite(go2, 0);
}

void TURN_LEFT()
{
  UNSET_MOTORS();
  digitalWrite(M12, HIGH);
  digitalWrite(M21, HIGH); 
  analogWrite(go, 255);
  analogWrite(go2, 255);
}

void TURN_RIGHT()
{
  UNSET_MOTORS();
  digitalWrite(M11, HIGH);
  digitalWrite(M22, HIGH); 
  analogWrite(go, 255);
  analogWrite(go, 255);
}

void SET_MOTORS_FORWARDS()
{
  digitalWrite(M11, HIGH);  
  digitalWrite(M21, HIGH); 
}

void SET_MOTORS_BACKWARDS()
{
  digitalWrite(M12, HIGH); 
  digitalWrite(M22, HIGH); 
}

void UNSET_MOTORS()
{
  digitalWrite(M11, LOW);  
  digitalWrite(M12, LOW); 
  digitalWrite(M21, LOW); 
  digitalWrite(M22, LOW); 
}
