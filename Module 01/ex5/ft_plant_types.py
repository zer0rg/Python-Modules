class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, \
              {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.5 + self.height * 0.05
        print(f"{self.name} provides {int(shade_area)} square meters of shade")

    def get_info(self):
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, \
            {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days,\
              {self.harvest_season} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("rose", 25, 30, "red")
    tulip = Flower("tulip", 20, 25, "yellow")

    oak = Tree("oak", 500, 1825, 50)
    pine = Tree("pine", 800, 3650, 70)

    tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("carrot", 30, 60, "autumn", "vitamin A")

    print(rose.get_info())
    rose.bloom()

    print(oak.get_info())
    oak.produce_shade()

    print(tomato.get_info())
    tomato.get_nutrition_info()
