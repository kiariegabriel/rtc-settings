import time
import board
import busio
import adafruit_ds3231
i2c = busio.I2C(board.SCL, board.SDA)

rtc = adafruit_ds3231.DS3231(i2c)

t=time.strftime('%H%M%S')
print(t)

rtc.datetime = time.struct_time((2020,9,24,int(t[:2]),int(t[2:4]),int(t[4:]),3,268,-1))
print(rtc.datetime)

