from lib.pulse import *


print("HR Calculator")

age = int(input("Enter age: "))
rest_rate = int(input("Enter rest heart rate: "))


max_hr = max_heart_rate(age)


print("\nYour zones:")
for zone_func in [
        vo2_zone, anaero_zone, aero_zone, call_burn_zone, light_activity_zone
    ]:
    lower, uppper = zone_func(max_hr, rest_rate)
    
    print("  {:16s}: {:d} - {:d}".format(zone_func.__name__[:-5],
                                                                lower, uppper))
