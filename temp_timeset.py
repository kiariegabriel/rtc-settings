import time
import board
import busio
import adafruit_ds3231
i2c = busio.I2C(board.SCL, board.SDA)

rtc = adafruit_ds3231.DS3231(i2c)


t=(2020, 8, 31, 24, 58, 25, 6, -1, -1)
rtc.datetime=time.struct_time(t)
t=rtc.datetime
print(t)
