def ft_plant_age():
    plant_age: int = 0
    try:
        plant_age = int(input("Enter plant age in days: "))
    except Exception:
        print("Plant age must be an integer")
        return ft_plant_age()
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
