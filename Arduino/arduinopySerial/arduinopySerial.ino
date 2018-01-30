#include <StopWatch.h>

StopWatch MySW;

int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int val_Left = 0;               // variable to store the value read of Left Diode
 
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  
int val_Right = 0;              // variable to store the value read of Right Diode

struct Packet {
  int start;
  unsigned long time_m;
  int left; 
  int right;
};

void setup() {
  Serial.begin(115200);          //  setup serial

/// setting the prescaler
//  ADCSRA &= ~(bit (ADPS0) | bit (ADPS1) | bit (ADPS2)); // clear prescaler bits

//  ADCSRA |= bit (ADPS0);                               //   2
//  ADCSRA |= bit (ADPS1) | bit (ADPS2);                 //  64
}

void loop() {
  Packet data = {255, micros(), analogRead(analogPin_Left), analogRead(analogPin_Right)};
//  int arr[] = {255, 1, 2, 63};
//  Serial.write((byte*)&data, sizeof(data));  // send data 
  Serial.println(sizeof(data));
}
