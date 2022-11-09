import network
import time
import machine

from utils import blink


def connect_net(essid, passwd):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    print('Connecting', essid)
    sta_if.connect(essid, passwd)
    cnt = 0
    _max = 5
    while not sta_if.isconnected() and not cnt > _max:       
        time.sleep(1)
        cnt += 1
    pre = ""
    if not sta_if.isconnected():
        pre = 'not'        
    print(".. %s connected" % pre)
        
    return sta_if.isconnected(), sta_if


def try_connect(wifis, reset_if_unconnected=False):
    connected = False
    sta_if = None
    for wifi in wifis:
        blink(1)
        connected, sta_if = connect_net(wifi[0], wifi[1])
        if connected and 2==1:
            import webrepl
            webrepl.start()
            webrepl._webrepl.password("pass")
            return connected, sta_if

    if not connected:
        # blink, wait, reset
        blink(2, 0.3)
        time.sleep(1)
        
        print("Machine reset in 3 s")
        blink(3, 0.5)
        time.sleep(3)
        
        machine.reset() 

    return connected, sta_if
