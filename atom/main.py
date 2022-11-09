import network
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('coworking', 'off1cep4ss')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()

try:
    import urequests
except:
    import upip
    upip.debug = True
    upip.install("micropython-urequests")
    import urequests
    
import json
import urequests as requests
#res = requests.get(url = 'http://172.16.2.227/meter/0').text
#print(res)

def get_sauna_temp():
    res = requests.get(url = 'http://172.16.2.108/api/heat/state').text
    sauna = json.loads(res)
    v = int(sauna['heat']['sensors'][0]['value']/100)
    print(sauna)
    return v


from time import sleep
from matrix import Matrix, self_test, Color, rotate_90


m = Matrix(rotator=rotate_90)
   
m.ticker("HALLO CHRISTOPH")
print("ticker end")
last_v = 0
recheck = 180
while True :
    color = Color.dark(Color.BLUE)
    v = get_sauna_temp()
    if v == last_v:
        print("no change")
        btn_pressed = m.wait_for_btn_pressed(recheck)
        if btn_pressed:
            break
        continue
    #if v < 25:
    #    color = Color.BLACK
    if v < 40:
        color = Color.dark(Color.BLUE)
    elif v < 50:
        color = Color.dark(Color.GREEN)
    elif v < 70:
        color = Color.dark(Color.YELLOW)
    elif v < 85:
        color = Color.ORANGE
    else:
        color = Color.RED
    text = "SAUNA "
    for _ in range(1):
        m.draw_word(text, sleep_time=0.3, color=color)
        m.clear()
        m.draw_word(str(v), sleep_time=0.5, color=color)
        m.clear()
        sleep(1)
    print("fill")
    m.fill(int(v/4), color)
    last_v = v
    
m.draw_word("ENDING")