class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


def create_plant(name: str, height: int, age: int):
    return Plant(name, height, age)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plant_configs = [
        ("rose", 25, 30),
        ("oak", 200, 365),
        ("cactus", 5, 90),
        ("sunflower", 80, 45),
        ("fern", 15, 120),
    ]

    plants = []
    for name, height, age in plant_configs:
        plant = create_plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.get_info()}")

    print(f"Total plants created: {len(plants)}")
