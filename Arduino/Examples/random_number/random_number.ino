int randNumber;

void setup(){
  Serial.begin(9600);
}

void loop() {

  randNumber = random(100, 300);
  Serial.println(randNumber);

  delay(100);
}
