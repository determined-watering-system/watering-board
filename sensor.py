from machine import ADC, Pin, I2C
import utime
from time import sleep

soil = ADC(Pin(27, Pin.IN)) # Soil moisture PIN reference
chip = ADC(4)

#Calibraton values
min_moisture=12883
max_moisture=49300

while True:
    # moisture = soil.read_u16()
#     moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    # print("moisture " + "%.2f" % moisture)
#     print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    print("HEY", soil.read_u16() * 3.3 / 65536)
#     cpu_voltage = chip.read_u16() * 3.3 / 65535
#     print("CPU", cpu_voltage)
#     print("CPU_TEMP", 27 - (cpu_voltage - 0.706)/0.001721)
    sleep(0.5)
