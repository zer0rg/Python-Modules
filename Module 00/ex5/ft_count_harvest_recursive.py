def ft_count_harvest_recursive():
    days_until_harvest = 0
    days_until_harvest = int(input("Days until harvest: "))

    def count(day):
        if day > days_until_harvest:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)

    count(1)
