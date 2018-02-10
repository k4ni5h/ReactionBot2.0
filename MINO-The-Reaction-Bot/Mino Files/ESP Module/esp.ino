#include<ESP8266WiFi.h>
#include<ESP8266WebServer.h>

ESP8266WebServer server;

char* ssid = "";              //enter the wifi network id
char* password = "";          // enter the wifi network password

uint8_t pin1 = 16;
uint8_t pin2 = 4;
uint8_t pin3 = 2;
void setup() {

  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  WiFi.begin(ssid, password);
  Serial.begin(115200);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }
  
  server.on("/11", on1);
  server.on("/21", on2);
  server.on("/31", on3);
  server.on("/10", off1);
  server.on("/20", off2);
  server.on("/30", off3);
  server.begin();

}

void loop() {
  server.handleClient();
}
void on1() {
  digitalWrite(pin1, HIGH);
  server.send(200, "text/plain", "Switch 1 is on");
}
void on2() {
  digitalWrite(pin2, HIGH);
  server.send(200, "text/plain", "Switch 2 is on");
}
void on3() {
  digitalWrite(pin3, HIGH);
  server.send(200, "text/plain", "Switch 3 is on");
}
void off1() {
  digitalWrite(pin1, LOW);
  server.send(200, "text/plain", "Switch 1 is off");
}
void off2() {
  digitalWrite(pin2, LOW);
  server.send(200, "text/plain", "Switch 2 is off");
}
void off3() {
  digitalWrite(pin3, LOW);
  server.send(200, "text/plain", "Switch 3 is off");
}

