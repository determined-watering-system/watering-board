import network
from time import sleep
import machine
import urequests

ssid = 'ssid'
password = 'pass'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def test_u_requests():
    r = urequests.get("http://date.jsontest.com")
    print("YO", r.json())
    r.close()
    
try:
    test_u_requests()
except KeyboardInterrupt:
    machine.reset()