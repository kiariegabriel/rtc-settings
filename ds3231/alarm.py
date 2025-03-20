import time
import board
import busio
import adafruit_ds3231
i2c = busio.I2C(board.SCL, board.SDA)

ds3231 = adafruit_ds3231.DS3231(i2c)

t=ds3231.datetime
t=list(t)
print(t)
t[5]=t[5]+30
if t[5]>60:
	t[5]=t[5]-60
	t[4]+=1
t=tuple(t)
print(t)
ds3231.alarm1 = (time.struct_time(t),'daily')
if ds3231.alarm1_status:
	print("wake up!")
	ds3231.alarm1_status = False

print('Alarm set. Check the SQW pin voltage')

time.sleep(30)

print('Alarm triggered. Check the SQW pin voltage')

#time.sleep(4)
"""

t2=ds3231.datetime
t2=list(t2)
print(t2)
t2[4]=t2[4]+2
t2=tuple(t2)
print(t2)
ds3231.alarm2 = (time.struct_time(t2), "daily")
if ds3231.alarm2_status:
        print("wake up!")
        ds3231.alarm2_status = False
"""
