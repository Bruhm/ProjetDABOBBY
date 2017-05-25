#ifndef PILOTAGE_H
#define PILOTAGE_H

#include "Arduino.h"
#include <Servo.h> 

static const int M11 = 12;
static const int M12 = 11;
static const int M22 = 7;
static const int M21 = 4;
static const int go = 3;
static const int go2 = 6;
static const int servoPin = 9; 
static const int Electromagnet = 8;
static const Servo Servo1; 

void INIT_MAGNET();
void MAGNET_OFF();
void MAGNET_ON();
void INIT_MOTORS_PINS();
void ALL_MOTORS_ON();
void ALL_MOTORS_OFF();
void TURN_LEFT();
void TURN_RIGHT();
void SET_MOTORS_FORWARDS();
void SET_MOTORS_BACKWARDS();
void UNSET_MOTORS();

#endif
