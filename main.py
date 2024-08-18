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

p1.setAddress(h1.getAddress())
p2.setAddress(h1.getAddress())
#print(h1)

print("\nlast time...")
print(p1)
print(p2)

print("\nRead a file...")
try:
	f = open("./values")
	for line in f:
		x = line.split()
		print("FirstName: " + x[0] + " MiddleName: " + x[1] + " LastName: " + x[2])
except:
	print("Exception!!!")
finally:
	f.close()
