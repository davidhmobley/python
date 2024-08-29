class Person:
    address = ""

    def setName(self, name):
        self.name = name

    def getName(self):
	    return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
	    return self.age

    def setEyeColor(self, color):
        self.eyeColor = color

    def getEyeColor(self):
	    return self.eyeColor

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
