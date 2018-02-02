int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  

struct Packet {
  unsigned long time_m;
  int left; 
  int right;
};


void InitADC(void){
  
  ADCSRA &= 0xf8;             // clear ADCSRA register
  ACSR = 0;
//  ADCSRB = 0;             // clear ADCSRB register

//  ADCSRA |= 0x01; // 2 prescaler
//  ADCSRA |= 0x02; // 4 prescaler
//  ADCSRA |= 0x03; // 8 prescaler
//  ADCSRA |= 0x04; // 16 prescaler
//  ADCSRA |= 0x05; // 32 prescaler
//  ADCSRA |= 0x06; //  64 prescaler
  ADCSRA |= 0x07; // 128 prescaler

  }

void setup() {
  Serial.begin(250000);          //  setup serial
  Serial.write("\n");         // 1 byte

//  InitADC();
}


void loop() {
   Packet data = {micros(), analogRead(analogPin_Left),analogRead(analogPin_Right)};
   Serial.write((byte*)&data, 8);
//   Serial.write("\n");
}
