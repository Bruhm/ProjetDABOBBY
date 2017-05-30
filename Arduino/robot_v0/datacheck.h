#ifndef DATACHECK_H
#define DATACHECK_H

#include "pilotage.h"
#define byte uint8_t

static const byte OK = 0;
static const byte ERROR_TELEMETER = 1;
static const byte ERROR_MOTOR= 1<<1;
static const byte ERROR_CAMERA = 1<<2;
static const byte ERROR_MAGNET = 1<<3;

byte CONTROL();
bool CHECK_TELEMETER();
bool CHECK_MOTOR();
bool CHECK_CAMERA();
bool CHECK_MAGNET();

#endif
