import Person
import House

p1 = Person.Person("David", 65, "blue")
p2 = Person.Person("Susan", 64, "green")
print("first time...")
print(p1)
print(p2)

h1 = House.House("780 Springvale Road", 24, "Red")
print("\nHouse...")
print(h1)

print("\nTest")
print(h1.getAddress())

p1.setAddress(h1.getAddress())
p2.setAddress(h1.getAddress())
#print(h1)

print("last time...")
print(p1)
print(p2)
