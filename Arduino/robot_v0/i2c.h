#ifndef I2C_H
#define I2C_H

#define byte uint8_t
#include <Wire.h>
#include "pilotage.h"

static const byte SLAVE_ADDRESS = 0x12;

void INIT_I2C();
void receiveData(int byteCount);
void dataCheck();

#endif
