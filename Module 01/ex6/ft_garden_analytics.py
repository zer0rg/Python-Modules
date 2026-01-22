class Plant:
    def __init__(self, name: str, height: int):
        self.name = name.capitalize()
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"

    @staticmethod
    def validate_height(height: int):
        return height > 0


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, flower_color: str):
        super().__init__(name, height)
        self.flower_color = flower_color

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.flower_color} \
            flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, flower_color: str, prize_points: int):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.flower_color} flowers \
            (blooming), Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.total_growth = 0
            self.plants_added = 0
            self.plant_type_count = {"regular": 0, "flowering": 0, "prize": 0}

        def record_growth(self, amount: int):
            self.total_growth += amount

        def record_plant(self, plant):
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.plant_type_count["prize"] += 1
            elif isinstance(plant, FloweringPlant):
                self.plant_type_count["flowering"] += 1
            else:
                self.plant_type_count["regular"] += 1

        def get_summary(self):
            return (
                f"Plants added: {self.plants_added}, Total growth: \
                    {self.total_growth}cm\n"
                f"Plant types: {self.plant_type_count['regular']} regular,"
                f"{self.plant_type_count['flowering']} flowering, "
                f"{self.plant_type_count['prize']} prize flowers"
            )

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)
        self.stats.record_plant(plant)

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            self.stats.record_growth(plant.height - initial_height)

    def calculate_score(self):
        return sum(plant.height for plant in self.plants)

    def show_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_summary())

    @classmethod
    def create_garden_network(cls, owners):
        return [cls(owner) for owner in owners]

    @classmethod
    def get_total_gardens(cls):
        return cls.total_gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    bob_garden.add_plant(Plant("Cactus", 15))
    bob_garden.add_plant(FloweringPlant("Tulip", 20, "pink"))

    alice_garden.grow_all()

    alice_garden.show_report()

    print(f"\nHeight validation test: {Plant.validate_height(25)}")

    print(
        f"\nGarden scores - Alice: {alice_garden.calculate_score()}, Bob:\
           {bob_garden.calculate_score()}"
    )

    print(f"\nTotal gardens managed: {GardenManager.get_total_gardens()}")
