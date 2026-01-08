from machine import Pin
import time

current = time.time() #for timing - LED lights with button

# setup
led = Pin(12, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
#     led.value(0) - LED lights no button
#     time.sleep(0.5)
#     led.value(1)
#     time.sleep(0.5)
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
    
elapsed = time.time() - current #for timing
