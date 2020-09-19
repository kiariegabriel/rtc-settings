import time
import board
import busio
import adafruit_ds3231
i2c = busio.I2C(board.SCL, board.SDA)

rtc = adafruit_ds3231.DS3231(i2c)

def time_list():
    t=rtc.datetime
    t=list(t)
    return t

def weekdays_shift():
    t=time_list()
    t[6]+=1
    if t[6]>6:
        t[6]=0
    print('Hooray!! Weekdays_shift checked')
    return t[6]

def year_shift():
    t=time_list()
    t[0]+=1
    print('Hooray!! year_shift checked')
    return t

def months_shift():
    t=time_list()
    t[1]+=1
    if t[1]>12:
        t=year_shift()
        t[1]=1
    print('Hooray!! monthss_shift checked')
    return t
        
def next_day():
    t=time_list()
    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    t[2]+=1
    t[6]=weekdays_shift()
    if t[2]<=days[t[1]]:
        t=(t[0],t[1],t[2],8,0,0,t[6],-1,-1)
    elif t[2]>days[t[1]]:
        t=months_shift()
        t[6]=weekdays_shift()
        t[2]=1
        t=(t[0],t[1],t[2],8,0,0,t[6],-1,-1)
    print('Hooray!! next_day checked')
    return t
    
    
def alarm_time1():
    t=time_list()
    t[3]=t[3]+1
    print(t)
    t=tuple(t)
    rtc.alarm1 = (time.struct_time(t), "daily")
    if rtc.alarm1_status:
        print("wake up!")
        rtc.alarm1_status = False

def alarm_time2():
    t=next_day()
    print(t)
    rtc.alarm1 = (time.struct_time(t), "daily")
    if rtc.alarm1_status:
        print("wake up!")
        rtc.alarm1_status = False


def alarm():
    t=time_list()
    print(t)
    t[3]=t[3]+1
    print(t[3])
    if t[3]<17:
        alarm_time1()
    elif t[3]==17 and t[4]<30:
        alarm_time1()
        print('Condition2 check')
    elif t[3]==17 and t[4]>=30:
        alarm_time2()
        print('Condition3 check')

    elif t[3]>=18:
        alarm_time2()
        print('Condition4 check')

    elif t[3]==25 and t[4]>=58:
        sleep(360)
        alarm_time2()
        print('Condition5 check')

alarm()
