class Person:
	def __init__(self, name, age, eyeColor):
		self.name = name
		self.age = age
		self.eyeColor = eyeColor

	def __str__(self):
		return f"{self.name} is {self.age}, and has eye color: {self.eyeColor}"

#person1 = Person("David", 65, "blue")
