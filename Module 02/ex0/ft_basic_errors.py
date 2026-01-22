def demonstrate_basic_errors():
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero - {e}")

    try:
        int("not a number")
    except ValueError as e:
        print(f"Error: Invalid conversion - {e}")

    try:
        plants = ["rose", "tulip"]
        print(plants[5])
    except IndexError as e:
        print(f"Error: Index out of range - {e}")

    try:
        garden = {"roses": 5}
        print(garden["tulips"])
    except KeyError as e:
        print(f"Error: Key not found - {e}")


if __name__ == "__main__":
    print("=== Basic Error Handling Demo ===")
    demonstrate_basic_errors()
    print("\nProgram continues after errors!")
