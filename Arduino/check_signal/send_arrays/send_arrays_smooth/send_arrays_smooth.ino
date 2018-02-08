int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  
int win_len = 20;

struct Packet {
  unsigned long time_m;
  int left; 
  int right;
};

#define FASTADC 1

// defines for setting and clearing register bits
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup() {

  #if FASTADC
     // set prescale (s=1, c=0) using table from https://forum.arduino.cc/index.php?topic=6549.0
     cbi(ADCSRA,ADPS2) ; 
     sbi(ADCSRA,ADPS1) ;
     cbi(ADCSRA,ADPS0) ;
  #endif
  
  Serial.begin(250000);       //  setup serial
  Serial.write("\n");         // 1 byte
  
}

Packet read_sensors(){
  int left = 0;
  int right = 0;
  for (int rep=0; rep < win_len; rep++){
    left += analogRead(analogPin_Left) / win_len;
    right += analogRead(analogPin_Right) / win_len;
  }
  Packet data = {micros(), left, right};
  return data;
}

void loop() {
   Packet data = read_sensors();
   Serial.write((byte*)&data, sizeof(data));
}
