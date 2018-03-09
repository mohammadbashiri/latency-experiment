int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  

bool led_state = 0;
int trial = 0;
int delay_count = 100;
int received_data = 0;

struct Packet {
  unsigned long time_m;
  int left; 
  int right;
  int trial_no;
  bool LED_state;
};

void setup() {

  // start seria comm
  Serial.begin(250000);       //  setup serial
  Serial.write("\n");         // 1 byte
  
}

void set_LEDs(short *array_of_LEDs, short array_size, bool level){
  for (int i=0; i<array_size; i++){
    digitalWrite(array_of_LEDs[i], level);
    }
  }

void loop() {
  if (Serial.available() > 0) {
    received_data = Serial.read();

    trial++;
    if (received_data == 65){
      led_state = 0;
    }

    if (received_data == 66){
      led_state = 1;
    }

    Packet data = {micros(), analogRead(analogPin_Left)/50, analogRead(analogPin_Right)/50, trial, led_state};
    Serial.write((byte*)&data, 11);
  }
}
