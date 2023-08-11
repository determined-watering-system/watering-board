from machine import Pin
from time import sleep

# relay_pin = 16
# led_pin = "LED"
# 
# relay = Pin(relay_pin, Pin.OUT)
# led = Pin(led_pin, Pin.OUT)
# 
# i = 0
# 
# while (i < 100):
#     i += 1
# #     relay.on()
#     relay.value(1)
# #     led.on()
#     led.value(1)
#     print("Open: ", i)
#     sleep(1)
#     relay.value(0)
# #     relay.off()
#     led.off()
#     print("Close: ", i)
#     sleep(1)

def relay_open(relay):
    return relay.value(1)

def relay_close(relay):
    return relay.value(0)

def water_for_sec(relay_pin, sec):
    relay = Pin(relay_pin, Pin.OUT)
    
    relay_open(relay)
    sleep(sec)
    relay_close(relay)
    