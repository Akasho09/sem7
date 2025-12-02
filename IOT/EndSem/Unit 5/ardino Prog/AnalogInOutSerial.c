int sensorPin = A0;
int ledPin = 9;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin); // 0–1023
  int outputValue = map(sensorValue, 0, 1023, 0, 255); // scale
  analogWrite(ledPin, outputValue);

  Serial.print("sensor = ");
  Serial.print(sensorValue);
  Serial.print("\t output = ");
  Serial.println(outputValue);

  delay(2);
}
