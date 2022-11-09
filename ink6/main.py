from inkplate6 import Inkplate
from image import *

import urequests
import network
from wifi import connect_net
from time import sleep



wifis = ['coworking','off1cep4ss']
connected, sta_if = connect_net(wifis[0], wifis[1]) 
print(connected)
print(sta_if.config())

#import upip
#upip.install("urequests")

display = Inkplate(Inkplate.INKPLATE_1BIT)

if __name__ == "__main__":
    display.begin()
    #display.clearDisplay()
    
    display.display()

    battery = str(display.readBattery())
    temperature = str(display.readTemperature())
    requests
    
    display.setTextSize(2)
    display.printText(20, 20, "batt: " + battery[:3] + "V")
    display.printText(20, 40, "TEMP: " + temperature + "C")
    display.display()
    sleep(3)
    
    display.drawBitmap(0, 0, "sd/gray_resiezed.bmp", 799, 600)
    display.display()
