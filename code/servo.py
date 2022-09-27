#Vincent Manka
#9/13/22
#make a servo rotate
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo
#imports servo library


pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
#sets pin number and frequency at which it spins


my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): 
        time.sleep(0.05)
        #makes the servo rotate 90 degrees back and forth