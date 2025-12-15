def ft_garden_summary():
    garden_name = input("Enter garden name: ")
    while True:
        try:
            number_of_plants = int(input("Enter number of plants: "))
            break
        except Exception:
            print("Number of plants must be an integer")
    print(f"Garden: {garden_name}")
    print(f"Plants: {number_of_plants}")
    print("Status: Growing well!")
