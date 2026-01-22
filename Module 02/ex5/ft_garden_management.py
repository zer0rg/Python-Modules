class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plants = {}

    def add_plant(self, plant_name, water_level=5, sunlight_hours=8):
        try:
            if not plant_name or plant_name.strip() == "":
                raise PlantError("Plant name cannot be empty!")

            if water_level < 1 or water_level > 10:
                raise PlantError(f"Invalid water level: {water_level}")

            if sunlight_hours < 2 or sunlight_hours > 12:
                raise PlantError(f"Invalid sunlight hours: {sunlight_hours}")

            self.plants[plant_name] = {
                "water_level": water_level,
                "sunlight_hours": sunlight_hours,
            }
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        try:
            print("Opening watering system")
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
        except Exception as e:
            print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        try:
            if plant_name not in self.plants:
                raise PlantError(f"Plant '{plant_name}' not found in garden!")

            plant = self.plants[plant_name]
            water = plant["water_level"]
            sun = plant["sunlight_hours"]

            if water < 1 or water > 10:
                raise WaterError(f"Water level {water} is too high (max 10)")

            if sun < 2 or sun > 12:
                raise PlantError(f"Sunlight hours {sun} out of range")

            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except (PlantError, WaterError) as e:
            print(f"Error checking {plant_name}: {e}")

    def simulate_water_shortage(self):
        raise GardenError("Not enough water in tank")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("Adding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 6, 7)
    garden.add_plant("", 5, 8)

    print()

    print("Watering plants...")
    garden.water_plants()

    print()

    print("Checking plant health...")
    garden.check_plant_health("tomato")
    garden.plants["lettuce"]["water_level"] = 15
    garden.check_plant_health("lettuce")

    print()

    print("Testing error recovery...")
    try:
        garden.simulate_water_shortage()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
