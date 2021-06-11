//Mini surveillance system

int motorPin1 =  5;    // Motor connected at pwm pin 5&6
int motorPin2 =  6;    
int IRsensor=2;        //IR sensor output connected at pwm pin2

String str="*";
float ival;
// The setup() method runs once, when the sketch starts

void setup()   {                
  // initialize the digital pins as an output:
  pinMode(motorPin1, OUTPUT); 
  pinMode(motorPin2, OUTPUT);  
  pinMode(IRsensor,INPUT);
  
  Serial.begin(4800);
  
}

// the loop() method runs over and over again,
// as long as the Arduino has power
void loop()                     
{
  rotateCW();
  rotateCCW();
  
}


void rotateCW(void){
  digitalWrite(motorPin1, HIGH); //rotates motor
  digitalWrite(motorPin2, LOW);    // set the Pin motorPin2 LOW
  for(int i=0;i<=180;i=i+2)
  {
    int status=digitalRead(IRsensor);
    if(status==HIGH)
    {
      ival=2.4;
    }
    else
    {
      ival=0.8;
    }
    delay(4500);
    Serial.println(i+str+ival);
  }
  digitalWrite(motorPin1, LOW); 
}

void rotateCCW(void){
  digitalWrite(motorPin2, HIGH); //rotates motor
  digitalWrite(motorPin1, LOW);    // set the Pin motorPin1 LOW
  for(int i=0;i<=180;i=i+2)
  {
    int status=digitalRead(IRsensor);
    if(status==HIGH)
    {
      ival=2.4;
    }
    else
    {
      ival=0.8;
    }
    delay(4500);
    Serial.println(i+str+ival);
  }
   digitalWrite(motorPin2, LOW);
}
