import os
import sys
import csv
import busio
import board
import datetime
import digitalio
from time import sleep
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


led=digitalio.DigitalInOut(board.D18)
led.direction=digitalio.Direction.OUTPUT


cs = digitalio.DigitalInOut(board.D5)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

mcp = MCP.MCP3008(spi, cs)

delay=2

def volt():
    channel = AnalogIn(mcp, MCP.P0)
    voltage=channel.voltage*2
    return voltage

date_object = str(datetime.date.today())
date_object='/home/pi/VoltageData/'+date_object+'.csv'

#This function saves the time and voltage readings in a CSV file format
#The file is saved with that specific day's date as the name
def voltage_csv():
    l1=[]
    now=datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    l1.extend((current_time,voltage))
    with open(date_object,mode='a') as file:
        create=csv.writer(file)
        create.writerow(l1)

try:
    while True:
        voltage=volt()
        print(voltage)
        voltage_csv()
        sleep(2)
        if voltage>=1.5 and voltage<=2:
            print('Voltage is low')
            sleep(0.5)
        elif voltage<1.5:
            print('voltage is extremely low!!!')
            sleep(delay)
            voltage=volt()
            if voltage>1.5 and voltage<2:
                print('Battery has recovered but still low!!!')
            elif voltage<=1.5:
                led.value=True
                sleep(1)
                led.value=True
#                os.system('shutdown now')
except KeyboardInterrupt:
        sys.exit()


