#include <Arduino.h>
#include <DeltaKinematics.h>

DeltaKinematics DK(100,300,35,112);

// Must specify this before the include of "ServoEasing.hpp"
#define USE_PCA9685_SERVO_EXPANDER    // Activating this enables the use of the PCA9685 I2C expander chip/board.
//#define PCA9685_ACTUAL_CLOCK_FREQUENCY 26000000L // Change it, if your PCA9685 has another than the default 25 MHz internal clock.
//#define USE_SOFT_I2C_MASTER           // Saves 1756 bytes program memory and 218 bytes RAM compared with Arduino Wire
//#define USE_SERVO_LIB                 // If USE_PCA9685_SERVO_EXPANDER is defined, Activating this enables force additional using of regular servo library.
//#define USE_LEIGHTWEIGHT_SERVO_LIB    // Makes the servo pulse generating immune to other libraries blocking interrupts for a longer time like SoftwareSerial, Adafruit_NeoPixel and DmxSimple.
//#define PROVIDE_ONLY_LINEAR_MOVEMENT  // Activating this disables all but LINEAR movement. Saves up to 1540 bytes program memory.
#define DISABLE_COMPLEX_FUNCTIONS     // Activating this disables the SINE, CIRCULAR, BACK, ELASTIC, BOUNCE and PRECISION easings. Saves up to 1850 bytes program memory.
#define MAX_EASING_SERVOS 3
//#define DISABLE_MICROS_AS_DEGREE_PARAMETER // Activating this disables microsecond values as (target angle) parameter. Saves 128 bytes program memory.
//#define DISABLE_MIN_AND_MAX_CONSTRAINTS    // Activating this disables constraints. Saves 4 bytes RAM per servo but strangely enough no program memory.
//#define DEBUG                         // Activating this enables generate lots of lovely debug output for this library.

//#define ENABLE_EASE_QUADRATIC
//#define ENABLE_EASE_CUBIC
//#define ENABLE_EASE_QUARTIC
//#define ENABLE_EASE_SINE
//#define ENABLE_EASE_CIRCULAR
//#define ENABLE_EASE_BACK
//#define ENABLE_EASE_ELASTIC
//#define ENABLE_EASE_BOUNCE
#define ENABLE_EASE_PRECISION
//#define ENABLE_EASE_USER

//#define PRINT_FOR_SERIAL_PLOTTER      // Activating this enables generate the Arduino plotter output from ServoEasing.hpp.
#include "ServoEasing.hpp"

#if defined(USE_PCA9685_SERVO_EXPANDER)
ServoEasing Servo1(PCA9685_DEFAULT_ADDRESS);
ServoEasing Servo2(PCA9685_DEFAULT_ADDRESS);
ServoEasing Servo3(PCA9685_DEFAULT_ADDRESS); // If you use more than one PCA9685 you probably must modify MAX_EASING_SERVOS
#else
ServoEasing Servo1;
ServoEasing Servo2;
ServoEasing Servo3;
#endif

#define START_DEGREE_VALUE  0 // The degree value written to the servo at time of attach.
//void blinkLED();


void setup() {
    //pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(115200);

#define SERVO1_PIN  0 // we use first port of expander
#define SERVO2_PIN  1 // we use first port of expander
#define SERVO3_PIN  2 // we use first port of expander

Servo1.attach(SERVO1_PIN, START_DEGREE_VALUE);
Servo2.attach(SERVO2_PIN, START_DEGREE_VALUE);
Servo3.attach(SERVO3_PIN, START_DEGREE_VALUE);
}

// Global variables to store current positions of each servo
float currentPos1 = 0;
float currentPos2 = 0;
float currentPos3 = 0;

void servoSimultaneous(float targetX, float targetY, float targetZ, int speed) {
  // Calculate the distance each servo needs to travel
  float distanceX = abs(targetX - currentPos1);
  float distanceY = abs(targetY - currentPos2);
  float distanceZ = abs(targetZ - currentPos3);

  // Find the maximum distance among all servos
  float maxDistance = max(max(distanceX, distanceY), distanceZ);

  // Calculate the total time required for all servos to reach their target positions
  float totalTime = maxDistance / speed;

  // Start time
  unsigned long startTime = millis();

  // Loop until all servos reach their target positions
  while (millis() - startTime < totalTime * 1000) {
    // Calculate the elapsed time
    float elapsedTime = (millis() - startTime) / 1000.0; // Convert milliseconds to seconds

    // Calculate the position for each servo based on elapsed time
    float posX = currentPos1 + (targetX - currentPos1) * (elapsedTime / totalTime);
    float posY = currentPos2 + (targetY - currentPos2) * (elapsedTime / totalTime);
    float posZ = currentPos3 + (targetZ - currentPos3) * (elapsedTime / totalTime);

    // Move all servos to their calculated positions simultaneously
    Servo1.write(posX);
    Servo2.write(posY);
    Servo3.write(posZ);
  }

  // Update current positions
  currentPos1 = targetX;
  currentPos2 = targetY;
  currentPos3 = targetZ;
}


void loop() {

  if (Serial.available()> 0){
    String dataString = Serial.readStringUntil('\n');
    int data[4];
    char* token = strtok((char*)dataString.c_str(), ",");
    int i = 0;
    while (token != NULL && i <= 3){
      data[i++] = atoi(token);
      token = strtok(NULL, ",");
    }

    //int value = Serial.parseInt();
    int x_value = data[0];
    int y_value = data[1];
    int z_value = data[2];
    int s_value = data[3];
    int speed = s_value;
    DK.x =  x_value;
    DK.y =  y_value;
    DK.z =  z_value;
    DK.inverse();
    servoSimultaneous(DK.x, DK.y, DK.z, speed);
    //delay(1000);
    
  }
}

/*
void blinkLED() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
}*/

