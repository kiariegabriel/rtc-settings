import time
import board
import busio
import adafruit_ds3231
i2c = busio.I2C(board.SCL, board.SDA)

ds3231 = adafruit_ds3231.DS3231(i2c)



if ds3231.alarm2_status:
        print("wake up!")
#        ds3231.alarm2_status = False

