from machine import Pin
from time import sleep

led=Pin("LED", Pin.OUT)

led.value(1)
sleep(5)
led.value(0)

