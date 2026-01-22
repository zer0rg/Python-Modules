class SecurePlant:
    def __init__(self, name: str):
        self._name = name.capitalize()
        self._height = 0
        self._age = 0

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        self._height = height
        print(f"Height updated: {height}cm [OK]")
        return True

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return False
        self._age = age
        print(f"Age updated: {age} days [OK]")
        return True

    def get_info(self):
        return f"{self._name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("rose")
    print(f"Plant created: {plant.get_name()}")

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)

    print(f"Current plant: {plant.get_info()}")
