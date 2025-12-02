int led = 13;

void setup() {
  pinMode(led, OUTPUT);      // configure pin as output
}

void loop() {
  digitalWrite(led, HIGH);   // LED on
  delay(1000);               // wait 1 second
  digitalWrite(led, LOW);    // LED off
  delay(1000);               // wait 1 second
}
