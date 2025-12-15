def ft_count_harvest_recursive():
    days_until_harvest = 0
    try:
        days_until_harvest = int(input("Days until harvest: "))
    except Exception:
        print("Days until harvest must be an integer")
        return ft_count_harvest_recursive()

    def count(day):
        if day > days_until_harvest:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)
    count(1)
