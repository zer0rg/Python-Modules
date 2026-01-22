class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_name):
    if plant_name == "tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water(water_level):
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_plant_error():
    try:
        print("Testing PlantError...")
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error():
    try:
        print("Testing WaterError...")
        check_water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_catching_all_garden_errors():
    print("Testing catching all garden errors...")

    errors_to_test = [lambda: check_plant("tomato"), lambda: check_water(5)]

    for test in errors_to_test:
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_catching_all_garden_errors()
    print("\nAll custom error types work correctly!")
