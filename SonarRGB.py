# Vincent
# 9/16/22
# sonar sensor that changes the color of a light

import digitalio
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel                       
from board import *

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Var = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Var.brightness = 0.1 #setting the brightness of the light, from 0-1 brightness
VarOutput = 0
Red = 0
Green = 0
Blue = 0

while True:
    try:
        cm = sonar.distance
        print((sonar.distance, Red, Green, Blue))
        time.sleep(0.01)
        if cm < 5:
            Blue = 0
            Green = 0
            Var.fill((255, 0, 0))#setting the color with RGB values
        elif cm > 5 and cm < 20:
            Green = 0
            Red = simpleio.map_range(cm, 5.1, 20, 255, 0)
            Blue = simpleio.map_range(Red, 0, 255, 255, 0)
            Var.fill((Red, Green, Blue))
        else:
            Blue = simpleio.map_range(cm, 20.1, 50, 255, 0)
            Green = simpleio.map_range(Blue, 0, 255, 255, 0)
            Var.fill((0, Green, Blue))#setting the color with RGB values
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.01)
