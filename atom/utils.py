from machine import Pin
import time
def blink(times=1, wait=0.1):
    
    # blink, wait, reset
    led = Pin(2, Pin.OUT)
    for i in range(times, 0, -1):
        led.value(1)
        time.sleep(wait)
        led.value(0)
        time.sleep(wait)
    led.value(1)