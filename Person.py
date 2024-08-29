class Person:
    address = ""

    def setAddress(self, addr):
        self.address = addr

    def getAddress(self):
	    return self.address

    def __init__(self, name, age, eyeColor):
        self.name = name
        self.age = age
        self.eyeColor = eyeColor
    
    def __str__(self):
        if self.address == "":
            return f"{self.name} is {self.age}. Has {self.eyeColor} eyes"
        else:
            return f"{self.name} is {self.age}. Has {self.eyeColor} eyes and lives at {self.address}"
