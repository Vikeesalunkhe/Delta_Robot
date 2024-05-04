void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // Set pin 13 as an output
}

void loop() {

  if (Serial.available()) {

    int delayValue = Serial.parseInt();

    for (int i=0; i<delayValue; i++) {
      digitalWrite(13, HIGH); // Turn on the LED (pin 13)
      delay(100); // Wait for 1 second
      digitalWrite(13, LOW); // Turn off the LED (pin 13)
      delay(100); // Wait for 1 second

    }
  
  }
}
