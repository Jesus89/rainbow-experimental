String input = "";
boolean complete = false;

void setup() {
  Serial.begin(9600);
  input.reserve(200);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  if (complete) {
    if (input == "on\n") {
      digitalWrite(13, HIGH);
    }
    else {
      digitalWrite(13, LOW);
    }
    input = "";
    complete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char c = (char)Serial.read();
    input += c;
    if (c == '\n') {
      complete = true;
    }
  }
}
