# Assignment 3 Question 1
# Amélie Cazelais and Kuljit Kaur

from machine import Pin, I2C
import i2c_lcd # in the lib folder
from time import sleep_ms
from hcsr04 import HCSR04

# setup
i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16) # 2 by 16 display
sensor = HCSR04(trigger_pin=Pin(25), echo_pin=Pin(34))

while True:
    lcd.clear()
    reading = sensor.distance_cm()
    print('Distance:', reading, 'cm')
    lcd.move_to(0,0) # cursor in top left
    lcd.putstr('Distance: %d cm' % reading)
    sleep_ms(1000)