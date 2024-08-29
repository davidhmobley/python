import Person
import House

# get users name
userName = ""
while userName == "":
	userName = input("What is your name? ")
	userName = userName.strip()
print("Welcome to python, " + userName + "!")
print("\tThere are " + str(len(userName)) + " characters in your name!")
for char in userName:
	print("\t\t" + char)

p1 = Person.Person("David", 65, "blue")
p2 = Person.Person("Susan", 64, "green")
# now, overwrite p2
p2.setName("Rebekah")
p2.setAge(29)
p2.setEyeColor("green")
print("\nfirst time...")
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
print("init nametypes")
fNames = []
fNamesSet = {""}
fNamesSet.clear()
mNames = []
mNamesSet = {""}
mNamesSet.clear()
lNames = []
lNamesSet = {""}
lNamesSet.clear()

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
			# no dups
			fNamesSet.add(x[0])
			mNamesSet.add(x[1])
			lNamesSet.add(x[2])
		elif len(x) == 2:
			print("FirstName: " + x[0] + " LastName: " + x[1])
			fNames.append(x[0])
			lNames.append(x[1])
			# no dups
			fNamesSet.add(x[0])
			lNamesSet.add(x[1])
		elif len(x) == 1:
			print("FirstName: " + x[0])
			fNames.append(x[0])
			# no dups
			fNamesSet.add(x[0])
except:
	print("Exception!!!")
finally:
	f.close()

# show nametypes
print("\nFirst Names (sorted)...")
fNames.sort()
print(fNames)
print("Middle Names (sorted)...")
mNames.sort()
print(mNames)
print("Last Names (sorted)...")
lNames.sort()
print(lNames)

# show nametypes w/o duplicates
print("\nFirst Names (no dups)...")
print(fNamesSet)
print("Middle Names (no dups)...")
print(mNamesSet)
print("Last Names (no dups)...")
print(lNamesSet)
