// Left LEDs: 11, 12, 13
// Right LEDs: 8, 9, 10

short Right_LED1 = 8;
short Right_LED2 = 9;
short Right_LED3 = 10;
short left_LED1 = 11;
short left_LED2 = 12;
short left_LED3 = 13;

void setup() {
  // initialize digital LED pin as an output.
  pinMode(Right_LED1, OUTPUT);
  pinMode(Right_LED2, OUTPUT);
  pinMode(Right_LED3, OUTPUT);
  pinMode(left_LED1, OUTPUT);
  pinMode(left_LED2, OUTPUT);
  pinMode(left_LED3, OUTPUT);
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

  // set the LEDs high or low
  set_LeftLEDs(LOW);
  set_RightLEDs(HIGH);
  delay(500);
  set_RightLEDs(LOW);
  set_LeftLEDs(HIGH);
  delay(500);  
}
