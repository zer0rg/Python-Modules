def ft_water_reminder():
    days_since_last = 0
    try:
        days_since_last = int(input("Days since last watering: "))
    except Exception:
        print("Days since last watering must be an integer")
        return ft_water_reminder()
    if days_since_last > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
