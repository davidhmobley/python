class House:

    def __str__(self):
        return f"{self.address} is {self.age} years old, and is {self.color}"

    def getAddress(self):
        return self.address
        
    def setAddress(self, addr):
        self.address = address

    def getAge(self):
	    return self.age

    def setAge(self, age):
	    self.age = age

    def getColor(self):
	    return self.color

    def setColor(self, color):
	    self.color = color

    def __init__(self, address, age, color):
        self.address = address
        self.age = age
        self.color = color
