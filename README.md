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


## Temperature Sensor


### Description & Code
I made an LCD display the temperature read by a temperature sensor
```python
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
import board
import analogio

# get and i2c object
i2c = board.I2C()
tmp36 = analogio.AnalogIn(board.A0)
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    lcd.set_cursor_pos(0, 0)
    lcd.print("Temp: {}C".format(temp_C))
    lcd.set_cursor_pos(1, 0)
    lcd.print("Temp: {}F".format(temp_F))
    time.sleep(.5)
   
```

### Evidence
![temperature](https://user-images.githubusercontent.com/71350243/225117088-87e99e77-41ed-4c23-a3b2-2e8967bb3f23.gif)
### Wiring
![temperature](https://user-images.githubusercontent.com/71350243/225462163-44105dc8-4b50-4f92-a96a-7d46805f07fb.png)
### Reflection
this project wasn't too hard and graham helped alot. the potentiometer at the back of the lcd backpack controls the brightness and contrast of the lcd. you also have to unplug the lcd when plugging in the micro usb.

## Rotary encoder

### Description & Code
I used a rotary encoder an LCD and LEDs to create a menu controlled stoplight.
```python
#Vincent
#3/28/23
#rotary encoder

import time

import rotaryio

import board

from lcd.lcd import LCD

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from digitalio import DigitalInOut, Direction, Pull



encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)

last_position = 0

btn = DigitalInOut(board.D1)

btn.direction = Direction.INPUT

btn.pull = Pull.UP

state = 0

Buttonyep = 1



i2c = board.I2C()

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)



ledGreen = DigitalInOut(board.D8)

ledYellow = DigitalInOut(board.D9)

ledRed = DigitalInOut(board.D10)

ledGreen.direction = Direction.OUTPUT

ledYellow.direction = Direction.OUTPUT

ledRed.direction = Direction.OUTPUT



while True:

    position = encoder.position

    if position != last_position:

        if position > last_position:

            state = state + 1

        elif position < last_position:

            state = state - 1

        if state > 2:

            state = 2

        if state < 0:

            state = 0

        print(state)

        if state == 0: 

            lcd.set_cursor_pos(0, 0)

            lcd.print("GOOOOO")

        elif state == 1:

            lcd.set_cursor_pos(0, 0)

            lcd.print("yellow")

        elif state == 2:

            lcd.set_cursor_pos(0, 0)

            lcd.print("STOPPP")

    if btn.value == 0 and Buttonyep == 1:

        print("buttion")

        if state == 0: 

                ledGreen.value = True

                ledRed.value = False

                ledYellow.value = False

        elif state == 1:

                ledYellow.value = True

                ledRed.value = False

                ledGreen.value = False

        elif state == 2:

                ledRed.value = True

                ledGreen.value = False

                ledYellow.value = False

        Buttonyep = 0

    if btn.value == 1:

        time.sleep(.1)

        Buttonyep = 1

    last_position = position
```

### Evidence

https://user-images.githubusercontent.com/91289762/226446966-8a585aef-7c21-480a-8ca3-219ae95f4cef.gif

### Wiring

![image](https://user-images.githubusercontent.com/71350243/228944301-c2f0f406-d630-4415-9ed6-08422b982cd2.png)
### Reflection

The code would not upload because vs code was down but kaz got a funtioning video

## Photointerruptor

### Description & Code

I used a photointeruptor and used code to count the number of passes the photointeruptor detects
```python
import time
import digitalio
import board

photoI = digitalio.DigitalInOut(board.D7)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP

last_photoI = True
last_update = -4

photoICrosses = 0

while True:
    if time.monotonic()-last_update > 4:
        print(f"The number of crosses is {photoICrosses}")
        last_update = time.monotonic()
    
    if last_photoI != photoI.value and not photoI.value:
        photoICrosses += 1
    last_photoI = photoI.value
```

### Evidence

![photointerruptor2](https://user-images.githubusercontent.com/71350243/228943496-eb766560-ca4f-453a-87c5-8876c54e69ca.gif)

### Wiring

![image](https://user-images.githubusercontent.com/71350243/228943572-2e0caafd-5b21-4b1a-a3b1-a24fae186c71.png)

### Reflection

Idk what this means

## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection

