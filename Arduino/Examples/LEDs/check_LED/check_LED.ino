// Left LEDs: 11, 12, 13
// Right LEDs: 8, 9, 10

short right_LEDs[] = {8, 9, 10}; 
short left_LEDs[] = {11, 12, 13};

int counter = 1;
bool SET_RightLED_HIIGH;

void setup() {
  // initialize digital LED pin as an output.
  for (int i=0; i<sizeof(right_LEDs); i++){
    pinMode(right_LEDs[i], OUTPUT);
    pinMode(left_LEDs[i], OUTPUT);
    }

  // set the LEDs high or low
  set_LEDs(left_LEDs, 3, LOW);
  set_LEDs(right_LEDs, 3, HIGH);
}

// function to set the LED set high or low
void set_LEDs(short *array_of_LEDs, short array_size, bool level){
  for (int i=0; i<array_size; i++){
    digitalWrite(array_of_LEDs[i], level);
    }
  }

void loop() {

  set_LEDs(left_LEDs, 3, LOW);
  set_LEDs(right_LEDs, 3, HIGH);
//  delay(500);
//  
//  set_LEDs(left_LEDs, 3, HIGH);
//  set_LEDs(right_LEDs, 3, LOW);
//  delay(500);
}
