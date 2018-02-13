/*
  Motor_PMW

  This program controls a relay and is more to use the PWM signal
  
  The circuit:
  - Motor relay attached from digital pin 9 to ground.

  created 13 Feb 2018
  by Nolan McCulloch
  

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Fading
*/

int MOTOR = 9;    // Motor connected to digital pin 9
int SPEED = 140;  // Min = 0 | Max = 255

void setup() {
  // nothing happens in setup
}

void loop() {
  
    analogWrite(MOTOR, SPEED);
    delay(5000); 
}
