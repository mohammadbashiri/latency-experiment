#include <StopWatch.h>

StopWatch MySW;

int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int val_Left = 0;               // variable to store the value read of Left Diode
 
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  
int val_Right = 0;              // variable to store the value read of Right Diode

float actual_value=0;

int incomingByte = 0;   // for incoming serial data


void setup() {

Serial.begin(19200);          //  setup serial
  
}

void loop() {

if (Serial.available() > 0) {
                
incomingByte = Serial.read(); // read the incoming byte:

  // send confirmation - ping test
  if(incomingByte == 68) // ord('D') = 68
  {
    Serial.println("Confirmation of connection to Arduino board!");
    }

  else if(incomingByte == 65) // ord('A') = 65 -> if 'A' is received
  {
    
//    MySW.reset(); // resets the measurement
//    MySW.start();
//    MySW.stop();
//    Serial.println(MySW.elapsed());

    val_Right = analogRead(analogPin_Right);
    actual_value= (5.0 * val_Right)/1024.0;     
    Serial.println(actual_value);     

   
  }                
  else if(incomingByte == 66) // ord('B') = 66 -> if 'B' is received
  {
    val_Left = analogRead(analogPin_Left);
    actual_value= (5.0 * val_Left)/1024.0;     
    Serial.println(actual_value); 
  } 
       
}
//delay(1000);
}
