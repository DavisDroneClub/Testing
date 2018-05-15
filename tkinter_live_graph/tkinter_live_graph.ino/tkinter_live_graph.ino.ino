double t = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  t = (double) millis();
  Serial.println("DATA;"+String(t/1000)+","+String(sin(t/1000)));
  delay(50);
}
