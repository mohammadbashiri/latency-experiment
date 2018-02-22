int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  

struct Packet {
  unsigned long time_m;
  unsigned int left; 
  unsigned int right;
};

void setup() {
  Serial.begin(250000);          //  setup serial
  Serial.write("\n");         // 1 byte
}

void loop() {
   Packet data = {micros(), analogRead(analogPin_Left), analogRead(analogPin_Right)};
   Serial.write((byte*)&data, 8);
}
