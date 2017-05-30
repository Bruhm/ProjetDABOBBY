int M11 = 12;
int M12 = 11;
int M22 = 7;
int M21 = 4;
int go = 3;
int go2 = 6;
int go10 = 10;
int luminosite = 0;

int pin_sharp = A0;  // fil jaune du capteur sharp branché a A0
//int pin_LED = 13; 

// the setup routine runs once when you press reset:
void setup() {
    // initialize the digital pin as an output.
    pinMode(M11, OUTPUT);
    pinMode(M12, OUTPUT);
    pinMode(M21, OUTPUT);
    pinMode(M22, OUTPUT);
    //pinMode(pin_LED,OUTPUT);
    Serial.begin(9600);  // initialisation communication série
    analogReference(EXTERNAL); // tension analogique max sera 3,3 V
                             // si AREF est relié  3,3 V
  //  analogWrite(go, 1000);
  //  digitalWrite(go10, HIGH);
  
  
}

// the loop routine runs over and over again forever:
void loop() {
  
  float distance = 32076.69016894*pow(valeur_moyenne(10), -1.245865753);
  Serial.println(distance);

  if (distance < 15) 
  {
    all_motors_off();
  }
  else if (distance > 15 && distance < 25)
  {
    turn_left();
  }
  else
  {
    all_motors_on();
  } 
}


void all_motors_on()
{
    set_motors();
    analogWrite(go, 255);
    analogWrite(go2, 255);
}

void all_motors_off()
{
    analogWrite(go, 0);
    analogWrite(go2, 0);
}

void turn_left()
{
  set_motors();
  analogWrite(go, 100);
  analogWrite(go2, 255);
}

void turn_right()
{
  set_motors();
  analogWrite(go, 100);
  analogWrite(go, 255);
}

void set_motors()
{
    digitalWrite(M11, HIGH);  
    digitalWrite(M12, HIGH); 
    digitalWrite(M21, HIGH); 
    digitalWrite(M22, HIGH); 
}

void unset_motors()
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
