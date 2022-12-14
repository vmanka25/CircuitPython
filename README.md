# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
I made the neopixel on the adafruit have epic gamer rgb

Code credit goes to [Phillip Burgess](https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython)
```python
#Vincent
#9/13/22
#rgb light transition
import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.NEOPIXEL

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 10

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
   # pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
  #  pixels.show()
  #  time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
   # pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
```


### Evidence
![helloworld](https://github.com/vmanka25/CircuitPython/blob/master/documentation/gamerRGB.gif?raw=true)

### Reflection
this project was pretty easy and I found the code online after doing the basic make it red thing. ctrl + to open terminal, and f5 to upload code to the adafruit


## CircuitPython_Servo

### Description & Code
I made two buttons control a servo using circuit python
```python
# Vincent
# 9/29/22
# 2 buttons that control the rotation of a servo

"""CircuitPython Essentials Servo standard servo example"""
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel
import board
import pwmio
from adafruit_motor import servo
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    time.sleep(.1)
    if btn == True:
        for angle in range(0, 180, 90):  # 0 - 180 degrees, 100 degrees at a time.
            my_servo.angle = angle
    elif btn2 == True:
        for angle in range(180, 0, -90): # 180 - 0 degrees, 100 degrees at a time.
            my_servo.angle = angle
    else:
        print("click a button man")
```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## Sonar rgb

### Description & Code
I made a neopixel change colors as the ultrasonic sensor senses different distances
```python
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
```

### Evidence
![sonarRGB](https://github.com/vmanka25/CircuitPython/blob/master/documentation/SonarRGB.gif?raw=true)

### Wiring
![sonar wiring](https://github.com/vmanka25/CircuitPython/blob/master/documentation/SonarRGB_wiring.png?raw=true)

### Reflection
At first i tried making the code withot simpleio and just math but it didn't work. someone else wrote working code before me so I used that code instead. in the future I will try and use the easier way. also importing the correct file from the lib is important.

## CircuitPython_LCD

### Description & Code
I made an lcd that displayed the clicks of buttons

code credit goes to [kaz](https://github.com/kshinoz98/CircuitPython)
```python
# Vincent
# 9/16/22
# lcd that displays clicks of buttons

import board
import math
import time
from lcd.lcd import LCD                                     #[4-14] code to connect 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface   #input pins to board
from digitalio import DigitalInOut, Direction, Pull
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP
num = 0                         #Display Variable
Redo = True                     #[16-17] Variable to "debounce" button

lcd.print("Starting")
while True:                                 #[19-30] Code to add and subtract 
    if btn.value == True and Redo == True:  #from variable and 
        if btn2.value == True:              #"debounce" the  #buttons.         
            num = num - 1
        else:
            num = num + 1                                   
        lcd.clear()
        lcd.print(str(num))
        Redo = False
        time.sleep(.1)
    elif btn.value == False and Redo == False:
        Redo = True



```

### Evidence
![lcdGIF](https://github.com/vmanka25/CircuitPython/blob/master/documentation/lcd.gif?raw=true)
### Wiring
![image](https://github.com/vmanka25/CircuitPython/blob/master/documentation/LcdWiring.png?raw=true)
### Reflection
this project was kind of difficult and I almost broke an adafruit. wiring buttons directly to 5v can short out the board, breaking it and hurting the computer. instead power the button directly from the pins on the adafruit like D2. 


## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
