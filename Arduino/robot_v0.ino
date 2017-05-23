#include <Wire.h>

#define SLAVE_ADDRESS 0x12
int dataReceived = 0;
int resolution = 100;
int uptime = 0;
int function_id = 0;

int M11 = 12;
int M12 = 11;
int M22 = 7;
int M21 = 4;
int go = 3;
int go2 = 6;
int go10 = 10;
int luminosite = 0;

int pin_sharp = A0;  // fil jaune du capteur sharp branché a A0

// the setup routine runs once when you press reset:
void setup() {
    // initialize the digital pin as an output.
    pinMode(M11, OUTPUT);
    pinMode(M12, OUTPUT);
    pinMode(M21, OUTPUT);
    pinMode(M22, OUTPUT);

    Serial.begin(9600);  // initialisation communication série
    analogReference(EXTERNAL); // tension analogique max sera 3,3 V
                             // si AREF est relié  3,3 V
  
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);
}


void receiveData(int byteCount){
    while(Wire.available()) {
        dataReceived = Wire.read();
        Serial.print("Donnee recue ");
        uptime = (dataReceived & 0xF);
        function_id = ((dataReceived >> 4) & 0xF);
        switch (dataReceived)
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
        }
        delay(uptime * resolution);
    }
}

void sendData(){
    int envoi = dataReceived + 1;
    Wire.write(uptime << 4 + function_id);
}

// the loop routine runs over and over again forever:
void loop() {

  /* float distance = 32076.69016894*pow(valeur_moyenne(10), -1.245865753);
  Serial.println(distance);

  all_motors_off();
  if (distance < 20) 
  {
    all_motors_off();
  }
  else if (distance > 20 && distance < 40)
  {
    turn_left();
  }
  else
  {
    all_motors_on();
  } */
  
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

float valeur_moyenne(float taille) {
  int total = 0;
  for (int i=0; i<taille; i++) {
    float lecture = analogRead(pin_sharp); 
    total = total + lecture;
    delay(10);
  }
  return(total/taille);
}
