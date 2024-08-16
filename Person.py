class Person:
#    House.House(House) == None
    address = ""

    def setAddress(addr):
        self.address = addr

    def __init__(self, name, age, eyeColor):
        self.name = name
        self.age = age
        self.eyeColor = eyeColor
    
    def __str__(self):
        return f"{self.name} is {self.age}, and has eye color: {self.eyeColor} and lives at {self.address}"
        
        
#person1 = Person("David", 65, "blue")
