// Left LEDs: 11, 12, 13
// Right LEDs: 8, 9, 10

short Right_LED1 = 8;
short Right_LED2 = 9;
short Right_LED3 = 10;
short left_LED1 = 11;
short left_LED2 = 12;
short left_LED3 = 13;

int analogPin_Left = 2;         // Left PhotoDiode connect on anaglog pin2  
int analogPin_Right = 3;        // Right PhotoDiode connect on anaglog pin3  

bool led_state = 0;
int trial = 0;
int counter = 1;

struct Packet {
  unsigned long time_m;
  int left; 
  int right;
  int trial_no;
  bool LED_state;
};

void setup() {
  
  // initialize digital LED pin as an output.
  pinMode(Right_LED1, OUTPUT);
  pinMode(Right_LED2, OUTPUT);
  pinMode(Right_LED3, OUTPUT);
  pinMode(left_LED1, OUTPUT);
  pinMode(left_LED2, OUTPUT);
  pinMode(left_LED3, OUTPUT);

  // set the LEDs high or low
  set_LeftLEDs(LOW);
  set_RightLEDs(HIGH);

  // start seria comm
  Serial.begin(250000);       //  setup serial
  Serial.write("\n");         // 1 byte
  
}

void set_LeftLEDs(bool level){
  digitalWrite(left_LED1, level);
  digitalWrite(left_LED2, level);
  digitalWrite(left_LED3, level);
  }

void set_RightLEDs(bool level){
  digitalWrite(Right_LED1, level);
  digitalWrite(Right_LED2, level);
  digitalWrite(Right_LED3, level);
  }

void loop() {
  // switch LEDs and send timing data

  if (counter%100==0 && led_state==0){
    set_LeftLEDs(HIGH);
    set_RightLEDs(LOW);
    led_state = 1;
    trial++;
    }
  else if (counter%100==0 && led_state==1){
    set_LeftLEDs(LOW);
    set_RightLEDs(HIGH);
    led_state = 0;
    trial++;
    }
    
  Packet data = {micros(), analogRead(analogPin_Left)/50, analogRead(analogPin_Right)/50, trial, led_state};
  Serial.write((byte*)&data, 11);
  
  counter++;
}
