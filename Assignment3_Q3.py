# Assignment 3 Question 3
# Amélie Cazelais and Kuljit Kaur

from machine import Pin, I2C
import i2c_lcd # in the lib folder
from time import sleep_ms
from hcsr04 import HCSR04

# setup
i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16) # 2 by 16 display

sensor = HCSR04(trigger_pin=Pin(25), echo_pin=Pin(34))

button = Pin(14, Pin.IN, Pin.PULL_UP)
last_state = 1
press_time = 0

# low and high readings
min_distance = 100
max_distance = 0

while True:
    lcd.clear()
    reading = sensor.distance_cm()
    print('Distance:', reading, 'cm')
    
    current_state = button.value()
    if last_state == 1 and current_state == 0:
        min_distance = 100
        max_distance = 0
        lcd.putstr('Min/Max Reset')
        sleep_ms(500)
    last_state = current_state
    
    lcd.move_to(0,0) # cursor in top left
    lcd.putstr('Distance: %d cm' % reading)
    lcd.move_to(0,1)
    if reading < min_distance:
        min_distance = reading
    if reading > max_distance:
        max_distance = reading
    lcd.putstr('Min:%d Max:%d' % (min_distance, max_distance))
    sleep_ms(1000)