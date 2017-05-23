int pin_sharp = A0;  // fil jaune du capteur sharp branché a A0


void setup() {
 
  Serial.begin(9600);  // initialisation communication série
  analogReference(EXTERNAL); // tension analogique max sera 3,3 V
                             // si AREF est relié  3,3 V
}

void loop() {

  float distance = 32076.69016894*pow(valeur_moyenne(10), -1.245865753);
  Serial.println(distance);
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
