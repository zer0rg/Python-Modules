def ft_harvest_total():
    day_count = 1
    total = 0
    while day_count <= 3:
        total += int(input(f"Day {day_count} harvest: "))
        day_count += 1
    print("Total harvest:", total)
