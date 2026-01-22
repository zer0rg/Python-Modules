def ft_water_reminder():
    days_since_last = 0
    days_since_last = int(input("Days since last watering: "))
    if days_since_last > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
