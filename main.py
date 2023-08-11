from machine import Pin
# from time import sleep
from time import localtime

from plants_config import plants_config, pins_config, night_time_start
from timer import skip_to_hour, skip_days
from relay import water_for_sec

# 
# led=Pin("LED", Pin.OUT)
# 
# led.value(1)
# sleep(5)
# led.value(0)

# min_sleeping_time_days = min(plants_config, key=)
def start():
    start_date = localtime()
    
#     {
#         plant_id: date[]
#     }
    watering_log = {
        "violet1": [],
        "succulent1": []
    }
    
    print("STARTING", start_date)
    
    def water_plant(plant):
        water_today(plant)
        watering_log[plant.id].push(localtime())
        print("WATERED!!!", plant.id)

    while True:
        if watering_log.length == 0:
            map(water_plant, plants_config)
        else:
            print("TODO")
        
        
        print("LOG FOR TODAY", watering_log)
        skip_days(1)
        
def get_plant_by_id(id):
    return next((item for item in plants_config if item["id"] == id), None)

def water_today(plant):
    skip_to_hour(night_time_start)
    
#     plant = get_plant_by_id(plant_id)
    
    water_for_sec(pins_config[plant["id"]], plant["watering_duration"])
    
    
start()

