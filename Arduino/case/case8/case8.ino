int M11 = 13;
int M12 = 12;
int M22 = 7;
int M21 =4;
int go = 3;
int go2 = 6;
int go10 = 10;

void setup() {

    pinMode(M11, OUTPUT);
    pinMode(M12, OUTPUT);
    pinMode(M21, OUTPUT);
    pinMode(M22, OUTPUT);
    analogWrite(go, 200);
    digitalWrite(go10, 200);
}

void loop() {
    digitalWrite(M11, LOW);  
    digitalWrite(M12, LOW); 
    digitalWrite(M21, LOW); 
    digitalWrite(M22, LOW); 
    analogWrite(go, 255);
    analogWrite(go2, 255);
}

