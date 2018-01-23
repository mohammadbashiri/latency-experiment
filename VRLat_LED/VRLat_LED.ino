#include <StopWatch.h>

StopWatch MySW;

int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int val_Left = 0;               // variable to store the value read of Left Diode
 
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  
int val_Right = 0;              // variable to store the value read of Right Diode

float actual_value=0;

int incomingByte = 0;   // for incoming serial data

int sensor_val[2];

void setup() {
  Serial.begin(9600);          //  setup serial
}

void loop() {
  val_Left  = analogRead(analogPin_Left); //
  val_Right = analogRead(analogPin_Right); //
  
  Serial.print(val_Left, BIN);
  Serial.print(",");
  Serial.println(val_Right, BIN);
  delay(10);
}
