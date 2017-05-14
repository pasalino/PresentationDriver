//INPUT
//You can change this with any digital input on Arduino
#define BACK 2
#define FORWARD 3

//OUTPUT
//You can change this with any digital output on Arduino
#define LED_BACK 8
#define LED_FORWARD 7

//SERIAL 
#define SERIAL_RATE 9600
#define BACK_TEXT "back\n"
#define FORWARD_TEXT "forward\n"

//ANTIBOUNCE DELAY
#define ANTIBOUNCE 200

//EDGE TRIGGERED VAR
int lastBackState = 0;
int lastForwardState = 0;

void setup() {
  //start serial connection
  Serial.begin(9600);

  //configure input output pin
  pinMode(BACK, INPUT);
  pinMode(FORWARD, INPUT);
  pinMode(LED_BACK, OUTPUT);
  pinMode(LED_FORWARD, OUTPUT);
}

void loop() {
  //read all input and Invert it (Use pull-up resistor in scheme)
  int backVal = not digitalRead(BACK);
  int forwardVal = not digitalRead(FORWARD);

  //Put back led on when press back Button
  digitalWrite(LED_BACK, backVal);
  //Put forward led on when press forward Button
  digitalWrite(LED_FORWARD, forwardVal);

  //Check if press Back Button
  if (risingEdgeCheck(backVal, lastBackState)) {
    Serial.write(BACK_TEXT);
    delay(ANTIBOUNCE);
  }

  //Check if press Forward Button
  if (risingEdgeCheck(forwardVal, lastForwardState)) {
    Serial.write(FORWARD_TEXT);
    delay(ANTIBOUNCE);
  }
}


//Check if current value is risingEdge Mode
bool risingEdgeCheck(int currentValue, int& lastValue) {
  //Check if is front
  if (currentValue == lastValue) return;
  //Update last value
  lastValue = currentValue;
  //Return if is rising front
  return currentValue == HIGH;
}

