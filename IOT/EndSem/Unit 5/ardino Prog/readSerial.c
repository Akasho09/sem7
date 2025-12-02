int pin = 2;

void setup(){
    pinMode(pin , INPUT);
    Serial.begin(9600);
}

void loop(){
    int state = digitalRead(pin);
    Serial.println(state);
    delay(100);
}

