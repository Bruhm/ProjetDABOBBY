#include "datacheck.h"

byte CONTROL()
{
  byte controlSum = 0;

   if(CHECK_TELEMETER()) controlSum += ERROR_TELEMETER;
   if(CHECK_MOTOR()) controlSum += ERROR_MOTOR;
   if(CHECK_CAMERA()) controlSum += ERROR_CAMERA;
   if(CHECK_MAGNET()) controlSum += ERROR_MAGNET; 
  
  return controlSum;
}

// Controle s'il y a une erreur dans le fonctionnement. Retourne vrai si une erreur est présente.

bool CHECK_TELEMETER() 
{
  bool check = false;
  return check;  
}

bool CHECK_MOTOR()
{
  bool check = false;
  return check;  
}

bool CHECK_CAMERA()
{
  bool check = false;
  return check;  
}

bool CHECK_MAGNET()
{
  bool check = false;
  return check;  
}

