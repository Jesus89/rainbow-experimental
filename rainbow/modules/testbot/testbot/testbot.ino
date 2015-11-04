#include "WS2812.h"

cRGB color;
WS2812 LED(1);

boolean led_enable = false;
boolean fade_enable = false;
float fade_inc = 0.004;
float fade_step = 0.004;
float fade_intensity = fade_step;

String input = "";
boolean complete = false;

void setup() {
  Serial.begin(9600);
  input.reserve(200);
  LED.setOutput(9);
  LED.setColorOrderRGB();
}

void loop() {
  if (complete) {
    if (input == "fon") {
      fade_enable = true;
      led_enable = false;
    }
    else if (input == "on") {
      fade_enable = false;
      led_enable = true;
    }
    else if (input[0] == '#') {
      color = convert_hex(input);
    }
    else if (input == "off") {
      fade_enable = false;
      led_enable = false;
      set_color(0, 0, 0);
    }
  input = "";
  complete = false;
  }
  if (fade_enable) {
    fade();
  }
  else if (led_enable) {
    set_color(color.r, color.g, color.b);
  }
}

void serialEvent() {
  while (Serial.available()) {
    char c = (char)Serial.read();
    complete = (c == '\n');
    if (!complete) { input += c; }
  }
}

void set_color(int r, int g, int b) {
  cRGB value;
  value.r = r;
  value.g = g;
  value.b = b;
  LED.set_crgb_at(0, value);
  LED.sync();
  delay(5);
}

cRGB convert_hex(String data) {
  cRGB color;
  long number = strtol( &data[1], NULL, 16);

  // Split them up into r, g, b values
  color.r = number >> 16;
  color.g = number >> 8 & 0xFF;
  color.b = number & 0xFF;
  return color;
}

void fade() {
  fade_intensity += fade_inc;
  if ((fade_intensity < fade_step) || (fade_intensity > 1.0)) {
    fade_inc *= -1;
  }

  int r = color.r * fade_intensity;
  int g = color.g * fade_intensity;
  int b = color.b * fade_intensity;

  set_color(r, g, b);
}
