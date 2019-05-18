const int sensorLuz = A4;
const int bocina = 10;
const int microfonoA = A3;
const int microfonoD = 9;
const int laser = 8;
const int frecuenciaBocinaSalida = 800;
int incomingByte;

void setup(){
  pinMode(sensorLuz, INPUT);
  pinMode(bocina, OUTPUT);
  pinMode(microfonoA, INPUT);
  pinMode(microfonoD, INPUT);
  pinMode(laser, OUTPUT);
  analogWrite(bocina, 0);
  Serial.begin(9600);
  digitalWrite(laser, LOW);
}

void loop(){
  if (Serial.available() > 0)
    {
      // read the incoming byte:
      incomingByte = Serial.read();
    }
    //imprimir sonido de punto
  if(incomingByte == '1'){ 
    tone(bocina, 1200, 1000);
    delay(1000);
  }
  //imprimir sonido de guion
  else if(incomingByte == '2'){ 
    tone(bocina, 1200, 3000);
    delay(1000);
  }
  //imprimir sonido de nada
  else if(incomingByte == '3'){ 
    delay(3000);
  }
  //imprimir luz punto
  else if(incomingByte == '4'){ 
    digitalWrite(laser, HIGH);
    delay(1000);
    digitalWrite(laser, LOW);
    delay(1000);
  }
  //imprimir luz guion
  else if(incomingByte == '5'){
    digitalWrite(laser, HIGH);
    delay(3000);
    digitalWrite(laser, LOW);
    delay(1000);
  }
  //imprimir luz nada
  else if(incomingByte == '6'){ 
    delay(3000);
  }
  //modo escucha para sonido
  else if(incomingByte == '7'){
  Serial.println(digitalRead(microfonoD));
    delay(20);
  }
  //modo escucha para luz
  else if(incomingByte == '8'){
    Serial.println(analogRead(sensorLuz));
    delay(20);
  }
  
  
  //Serial.println(analogRead(microfonoA));
  //Serial.println();
}
