#include "pilotage.h"

void INIT_MAGNET() { 
   
   Servo1.attach(servoPin);
   pinMode(Electromagnet, OUTPUT); 
   digitalWrite(Electromagnet, LOW);
   Servo1.write(0);
}

void MAGNET_ON(){ 

  digitalWrite(Electromagnet, HIGH);
}

void MAGNET_OFF(){ 

  digitalWrite(Electromagnet, LOW);
}

float valeur_moyenne(float taille) {
  int total = 0;
  for (int i=0; i<taille; i++) {
    float lecture = analogRead(pin_sharp); 
    total = total + lecture;
    delay(10);
  }
  return(total/taille);
}
void SERVO_ON(){ 

  Servo1.write(90);
}

void SERVO_OFF(){ 

  Servo1.write(0);
}

void INITIALISATION(){
    INIT_MAGNET();
    INIT_MOTORS_PINS();
}

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
}

void TURN_RIGHT()
{
  UNSET_MOTORS();
  digitalWrite(M11, HIGH);
  digitalWrite(M22, HIGH); 
}

void SET_MOTORS_FORWARDS()
{
  UNSET_MOTORS();
  digitalWrite(M11, HIGH);  
  digitalWrite(M21, HIGH); 
}

void SET_MOTORS_BACKWARDS()
{
  UNSET_MOTORS();
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
