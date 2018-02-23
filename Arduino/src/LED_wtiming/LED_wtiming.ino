// Left LEDs: 11, 12, 13
// Right LEDs: 8, 9, 10

short right_LEDs[] = {8, 9, 10}; 
short left_LEDs[] = {11, 12, 13}; 

int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  

bool led_state = 0;
int trial = 0;
int counter = 1;
int delay_count;

struct Packet {
  unsigned long time_m;
  int left; 
  int right;
  int trial_no;
  bool LED_state;
};

void setup() {
  
  // initialize digital LED pin as an output.
  for (int i=0; i<sizeof(right_LEDs); i++){
    pinMode(right_LEDs[i], OUTPUT);
    pinMode(left_LEDs[i], OUTPUT);
    }

  // set the LEDs high or low
  set_LEDs(left_LEDs, 3, LOW);
  set_LEDs(right_LEDs, 3, HIGH);

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
  
  // switch LEDs and send timing data

  delay_count = random(100, 300);
  
  if (counter%delay_count==0 && led_state==0){
    set_LEDs(left_LEDs, 3, HIGH);
    set_LEDs(right_LEDs, 3, LOW);
    led_state = 1;
    trial++;
    }
  else if (counter%delay_count==0 && led_state==1){
    set_LEDs(left_LEDs, 3, LOW);
    set_LEDs(right_LEDs, 3, HIGH);
    led_state = 0;
    trial++;
    }
    
  Packet data = {micros(), analogRead(analogPin_Left)/50, analogRead(analogPin_Right)/50, trial, led_state};
  Serial.write((byte*)&data, 11);
  
  counter++;
}
