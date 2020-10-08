# Created by: Evan
# Created on: Oct.2020
# This program controls a servo with a potentiomketer

from microbit import *



pin2.set_analog_period(10)
display.show(Image.HEART)

while True:
    potentiometer = pin1.read_analog()
    potentiometer = potentiometer/5.683333
    if potentiometer < 40:
        potentiometer = 40
    pin2.write_analog(int(potentiometer))
    print(int(potentiometer))
    sleep(500)


