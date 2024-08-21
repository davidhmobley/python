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

# lists of nametypes
fNames = []
mNames = []
lNames = []

print("\nRead a file...")
try:
	f = open("./values")
	for line in f:
		x = line.split()
		if len(x) == 3:
			print("FirstName: " + x[0] + " MiddleName: " + x[1] + " LastName: " + x[2])
			fNames.append(x[0])
			mNames.append(x[1])
			lNames.append(x[2])
		elif len(x) == 2:
			print("FirstName: " + x[0] + " NoMiddleName LastName: " + x[1])
			fNames.append(x[0])
			lNames.append(x[1])
		elif len(x) == 1:
			print("FirstName: " + x[0] + " NoMiddleName NoLastName")
			fNames.append(x[0])
except:
	print("Exception!!!")
finally:
	f.close()

# show nametypes
print("\nFirst Names...")
print( fNames)
print("Middle Names...")
print( mNames)
print("Last Names...")
print(lNames)
