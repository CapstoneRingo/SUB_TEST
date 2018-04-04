#include <time.h>
#include <string.h> 
#include <SoftwareSerial.h>

#define RELAY_CH_1 1
#define RELAY_CH_2 2
#define RELAY_CH_3 3
#define RELAY_CH_4 4
#define RELAY_CH_5 5
#define RELAY_CH_6 6
#define RELAY_CH_7 7
#define RELAY_CH_8 8
#define LED_PIN    13

#define WRITE_MODE 0        // BOOL - 0, run in loop 1, listen

int count = 0; 

void setup() {
  // put your setup code here, to run once:
  pinMode(RELAY_CH_1, OUTPUT);
  pinMode(RELAY_CH_2, OUTPUT);
  pinMode(RELAY_CH_3, OUTPUT);
  pinMode(RELAY_CH_4, OUTPUT);
  pinMode(RELAY_CH_5, OUTPUT);
  pinMode(RELAY_CH_6, OUTPUT);
  pinMode(RELAY_CH_7, OUTPUT);
  pinMode(RELAY_CH_8, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  digitalWrite(RELAY_CH_1, LOW);
  digitalWrite(RELAY_CH_2, LOW);
  digitalWrite(RELAY_CH_3, LOW);
  digitalWrite(RELAY_CH_4, LOW);
  digitalWrite(RELAY_CH_5, LOW);
  digitalWrite(RELAY_CH_6, LOW);
  digitalWrite(RELAY_CH_7, LOW);
  digitalWrite(RELAY_CH_8, LOW);
  digitalWrite(LED_PIN, LOW); 

  Serial.begin(9600); 
  while(!Serial) {
    delay(100); 
  }
}

void flash(int flashItter) {
  for(int i = 0; i < flashItter; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(250);
    digitalWrite(LED_PIN, LOW); 
    delay(250); 
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Ready to start Pneumatics control.\nStarting Seqence\n");

  // TEST SEQUENCE

  while(WRITE_MODE == 0) {
    Serial.println("Iteration: " + String(count));
    count++;
    
    digitalWrite(RELAY_CH_1, HIGH);
    flash(1);
    delay(200); 
    digitalWrite(RELAY_CH_2, HIGH);
    flash(2);
    delay(200); 
    digitalWrite(RELAY_CH_3, HIGH);
    flash(3);
    delay(200); 
    digitalWrite(RELAY_CH_4, HIGH);
    flash(4);
    delay(200);
    digitalWrite(RELAY_CH_5, HIGH);
    flash(5);
    delay(200);
    digitalWrite(RELAY_CH_6, HIGH);
    flash(6);
    delay(200);
    digitalWrite(RELAY_CH_7, HIGH);
    flash(7);
    delay(200);
    digitalWrite(RELAY_CH_8, HIGH);
    flash(8);
    delay(2000);

    digitalWrite(RELAY_CH_1, LOW);
    flash(1);
    delay(200); 
    digitalWrite(RELAY_CH_2, LOW);
    flash(2);
    delay(200); 
    digitalWrite(RELAY_CH_3, LOW);
    flash(3);
    delay(200); 
    digitalWrite(RELAY_CH_4, LOW);
    flash(4);
    delay(200);
    digitalWrite(RELAY_CH_5, LOW);
    flash(5);
    delay(200);
    digitalWrite(RELAY_CH_6, LOW);
    flash(6);
    delay(200);
    digitalWrite(RELAY_CH_7, LOW);
    flash(7);
    delay(200);
    digitalWrite(RELAY_CH_8, LOW);
    flash(8);
    delay(2000);
  }

  // CONSOLE CONTROL
  if (Serial.available() > 0) {
     //inByte = Serial.read(); 
    Serial.println("Printing stuff: ");
  }
  

}
