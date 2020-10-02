import digitalio
from board import *
import time

led = digitalio.DigitalInOut(D18)
led.direction = digitalio.Direction.OUTPUT
print('Blink led active!')
for i in range 5:

    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(0.5)
