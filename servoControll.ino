#include <Servo.h>  // Servo kütüphanesini ekliyoruz.
  // Servo kontrol potunu bağlayacağımız analog giriş.
Servo servo;      // Bu komutla servo kontrol nesnemizi oluşturduk   

void setup(){
  servo.attach(9);
  Serial.begin(9600);
  servo.write(0);
} 
void loop(){
  if(Serial.available()) {
    int oku = Serial.read();
    if(oku == '0') {
      servo.write(50);
    }else if(oku == '1') {
      servo.write(0);
    } 
  }
}


