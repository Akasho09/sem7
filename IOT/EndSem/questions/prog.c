/*
Write a program for Arduino Board that collects 10 readings from an analog sensor and stores them in an array. 
It then calculates a running average each time a new reading is added. Discuss how this method helps smooth out sudden changes 
in the data and avoid any delay in getting the average.
*/
#include <stdio.h>

int i = 0;
int v[10];

void setup(){
    Serial.begin(9600);
    for(int i=0;i<10;i++) v[i]=0;
}

void loop(){
    int avg = 0 ;
        int reading = analogRead(A0);
        avg = (avg-v[i]+reading)/10;
        v[i]=reading;
        i = (i+1)%10;
        Serial.println(avg);
        delay(100);
}

