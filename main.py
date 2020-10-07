# Created by: Evan
# Created on: Oct.2020
# This program reads the value of a potentiometer

from microbit import *



pin2.set_analog_period(10)

while True:
    potentiometer = pin1.read_analog()
    
    pin2.write_analog(potentiometer)
    sleep(200)


