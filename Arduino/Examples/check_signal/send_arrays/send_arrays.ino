struct Packet {
   long t;
};


void setup() {
  Serial.begin(250000); //  setup serial
  Serial.write("\n");
}

void loop() {
  Packet packet = {micros()};
  Serial.write((byte*)&packet, 4);  // send data 
  
}
