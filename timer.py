from time import sleep, localtime

def days_to_sec(days):
    return days * 24 * 60 * 60

def hours_to_sec(hours):
    return hours * 60 * 60

def skip_days(days):
    sleep(days_to_sec(days))
    
def get_hours_diff(hour1, hour2):
    return hour1 < hour2 ? hour2 - hour1 : 24 - hour1 + hour2

def skip_to_hour(hour, hour_until):
#     hour_now = datetime.now().time().hour
    hour_now = localtime()[4]
    print("NOW", hour_now)
    hours_to_sleep = get_hours_diff(hour_now, hour_until)
    print("SLEEP", hours_to_sleep)
    sleep(hours_to_sec(hours_to_sleep))