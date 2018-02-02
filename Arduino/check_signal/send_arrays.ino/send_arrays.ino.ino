
void setup() {
  Serial.begin(250000); //  setup serial
}

void loop() {
  Serial.write(micros());  // send data 
}
