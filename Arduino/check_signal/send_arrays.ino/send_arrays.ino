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


uint8_t exponent(uint8_t mantissa, uint16_t x) {
  // Compute the exponent of a powered value
  // Same as exponent = Ln(x)/Ln(mantissa) but quick and dirty
      uint8_t exp = 0;
      uint16_t result = 1;
      while (x != result) {
          result *= mantissa;
          exp++;
      }
      // Returned value
      return (exp);
}


void setup() {
  Serial.begin(250000);          //  setup serial

  // Compute adc prescaler value automatically
  uint8_t adcPrescaler = 128; // Allowed values are ranging from 2^1 to 2^7
  
  // Set prescaler
  uint8_t adcPrescalerExponent = exponent(2, adcPrescaler);
  ADCSRA |= (adcPrescalerExponent >> 1);
}


void send2ByteValue(int value){

 // big endian
  
  Serial.write(value >> 8);
  Serial.write(value);
  
  }

void send4ByteValue(uint32_t value){
  
  Serial.write(value >> 24);
  Serial.write(value >> 16);
  Serial.write(value >> 8);
  Serial.write(value);
  
  }



void loop() {
//  Packet data = {255, micros(), analogRead(analogPin_Left), analogRead(analogPin_Right)};
//  int arr[] = {255, 1, 2, 63};
//  Serial.write((byte*)&data, sizeof(data));  // send data 
//  Serial.println(sizeof(data));

//millis() returns unsigned long which is 4 bytes

//Serial.write("X");        // 1 byte
send4ByteValue(millis());   // 4 byte
//Serial.write(",");          // 1 byte
Serial.write(analogRead(analogPin_Left));       // 1 byte
//Serial.write(",");          // 1 byte
Serial.write(analogRead(analogPin_Right));       // 1 byte
Serial.write("\n");         // 1 byte
}
