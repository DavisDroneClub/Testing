int inByte = 0;
String inString;
String parse_head, parse_data;
int delimIndex;
int interval = 10;
long prevTime;
int count = 0;
String hbtString = "HBT;";

void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  prevTime = millis();
}

void loop(){
  if(Serial.available()>0){
    inString = "";
    while(Serial.available()>0){
      delay(3);
      inString += char(Serial.read());
    }
    
    delimIndex = inString.indexOf(',');
    parse_head = inString.substring(0,delimIndex);
    parse_data = inString.substring(delimIndex + 1);
    Serial.println(parse_head);
    if(parse_head == "CMD")
    {
      digitalWrite(13,HIGH);
      delay(parse_data.toInt()*1000);
      digitalWrite(13,LOW);
    }
    else if(parse_head == "ECHO")
    {
      Serial.println(parse_data);
    }
  }
  
  if((millis()-prevTime)> interval){
    Serial.println(hbtString+count);
    count++;
    prevTime = millis();
  }
  
  
}
