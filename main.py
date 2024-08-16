import Person
import House

p1 = Person.Person("David", 65, "blue")
p2 = Person.Person("Susan", 64, "green")
print(p1)
print(p2)

h1 = House.House("780 Springvale Road", 24, "Red")
print(h1)

p1.setHouse(h1)
p2.setHouse(h1)
#print(h1)

print(p1)
print(p2)
