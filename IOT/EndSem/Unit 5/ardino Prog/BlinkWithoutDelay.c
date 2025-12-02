const int ledPin = 13;
unsigned long previousMillis = 0;
const long interval = 1000;   // 1 s

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    // toggle LED
    int state = digitalRead(ledPin);
    digitalWrite(ledPin, !state);
  }

}
