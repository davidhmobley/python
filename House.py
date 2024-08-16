class House:
	def __init__(self, address, age, color):
		self.address = address
		self.age = age
		self.color = color

	def __str__(self):
		return f"{self.address} is {self.age} years old, and is {self.color}"
