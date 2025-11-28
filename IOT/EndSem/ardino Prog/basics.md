## Arduino Mega Programmming basics 
The Arduino Mega 2560 is a powerful microcontroller board with `54` digital pins, `16` analog inputs, and 4 serial ports. Programming it is easy using the Arduino IDE.

1. Structure of Every Arduino Program
- An Arduino program (also called a sketch) has two main functions:

- ✔️ setup()
    - Runs only once when the board starts.
    - Used to initialize pins, serial communication, sensors, etc.
- ✔️ loop()
    - Repeats continuously until the board is powered off.
    - Used for the main logic of your program.

2. Digital Output (Turning an LED On/Off)
- Set a pin as output
- Write HIGH or LOW to it
```c
void setup() {
  pinMode(13, OUTPUT);   // LED pin
}

void loop() {
  digitalWrite(13, HIGH);  // Turn ON
  delay(1000);
  digitalWrite(13, LOW);   // Turn OFF
  delay(1000);
}
```

3. Digital Input (Reading a Button)

```c
int button = 7;

void setup() {
  pinMode(button, INPUT);
  Serial.begin(9600);
}

void loop() {
  int state = digitalRead(button);
  Serial.println(state);
  delay(100);
}
```

4. Analog Input (Reading Sensors)
- Arduino Mega has 16 analog pins (A0–A15).
```c
void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(A0); // 0 to 1023
  Serial.println(value);
  delay(200);
}
```

| **Function**                  | **Use**                  |
| ----------------------------- | ------------------------ |
| `pinMode(pin, OUTPUT)`        | set pin as output        |
| `pinMode(pin, INPUT)`         | set pin as input         |
| `digitalWrite(pin, HIGH/LOW)` | digital output           |
| `digitalRead(pin)`            | read digital input       |
| `analogRead(pin)`             | read analog sensor value |
| `analogWrite(pin, value)`     | write PWM output         |
| `delay(ms)`                   | pause for milliseconds   |
| `Serial.begin(baud)`          | start serial             |
| `Serial.print(), println()`   | print data               |


### 10. First Program (Blink Example)
```c

void setup(){
    pinMode(10,OUTPUT); 
}

void loop(){
    displaypin(10,HIGH);
    DELAY(1000);
    displaypin(10,low);
    DELAY(1000);
}

```

### Arduino Mega Program: Fade 12 LEDs Up and Down One by One

```c
int ledPins[12] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

void setup(){
    for(int i=0;i<12;i++) pinMode(ledPins[i],OUTPUT);
}

void loop(){
    for(int i=0;i<12;i++) {
        for(int brightness=0;brightness<255;brightness++){
            analogWrite(pin[i],brightness);
            delay(5);
        }
        for(int brightness=255;brightness>=0;brightness--){
            analogWrite(pin[i],brightness);
            delay(5);
        }
    }
}

```