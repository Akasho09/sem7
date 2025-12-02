const int sensorPin = A0;
int readings[10];      
int index = 0;
long total = 0; 
int average = 0;

void setup() {
  Serial.begin(9600);

  // initialize array
  for (int i = 0; i < 10; i++) {
    readings[i] = 0;
  }
}

void loop() {
  // subtract old value
  total = total - readings[index];

  // take new reading
  readings[index] = analogRead(sensorPin);

  // add new value
  total = total + readings[index];

  // move to next index
  index = index + 1;

  if (index >= 10) index = 0;

  // compute average
  average = total / 10;

  Serial.println(average);
  delay(100);
}
