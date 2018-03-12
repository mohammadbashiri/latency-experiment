int received_data = 0;

void setup() {
  Serial.begin(250000);          //  setup serial
  Serial.write("\n"); 
}

void loop() {
  if (Serial.available() > 0) {
    received_data = Serial.read();
     Serial.write("Confirmation of receiving data: ");
     Serial.write(received_data);
     Serial.write('\n');
  }
}
