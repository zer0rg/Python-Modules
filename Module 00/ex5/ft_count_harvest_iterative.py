def ft_count_harvest_iterative():
    days_until_harvest = 0
    i = 1
    try:
        days_until_harvest = int(input("Days until harvest: "))
    except Exception:
        print("Days until harvest must be an integer")
        return ft_count_harvest_iterative()
    while i <= days_until_harvest:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
