class Plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name.capitalize()
		self.height = height
		self.age_days = age

	def get_info(self):
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")

	def grow(self):
		self.height += 1

	def age(self):
		self.age_days += 1

	def pass_day(self):
		self.grow()
		self.age()


if __name__ == "__main__":
	i = 1
	rose = Plant("rose", 25, 30)
	initial_height = rose.height
	while i <= 7:
		if i == 1 or i == 7:
			print(f"=== Day {i} ===")
			rose.get_info()
		rose.pass_day()
		i += 1
	print(f"Growth this week: +{rose.height - initial_height}cm")
