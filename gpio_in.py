import time
import board
import digitalio
 
print("hello blinky!")
 
#led = digitalio.DigitalInOut(board.D18)
#led.direction = digitalio.Direction.INPUT
 
#while True:
#    led.value = True
#    time.sleep(2)
#    led.value = False
#    time.sleep(2)
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
