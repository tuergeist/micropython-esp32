import network
import time
import machine



def connect_net(essid, passwd):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.scan()
    time.sleep(1)
    print(sta_if.config('mac'))
    print('Connecting', essid)
    sta_if.disconnect()
    cnt = 0
    _max = 5
    while not cnt > _max:
        try:
            sta_if.connect(essid, passwd)
        except OSError as e:
            print(e)
            time.sleep(1)
            cnt += 1
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
        connected, sta_if = connect_net(wifi[0], wifi[1])
        if connected:
            #import webrepl
            #webrepl.start()
            #webrepl._webrepl.password("pass")
            return connected, sta_if

    if not connected:
        # blink, wait, reset
        print("Machine reset in 3 s")
        time.sleep(3)
       
        machine.reset() 

    return connected, sta_if
