import random

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)



# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x + y + z)

# x = 5
# y = "John"
# print(x, y)


x = "awesome"

def myfunc():
  global x 
  x= "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

x = 5
print(type(x))
  
# print(random.randrange(1,10));


# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')


# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

a = "  Hello, World!  "
print(a[0])


for x in 'vivek':
  print(x)

print('ld' in a)

print('ld' not in a)

print(a[-8:-2])

print(a.upper())

print(a.strip())

print(a.replace('H','J'))

print(a.split(','))


# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

b="hello world"

print(b.capitalize())

print(b.encode())

print(bool("Hello"))
print(bool(15))

print(2//3)

x=2;

print(x)

print(x<<2)
# method 1 to create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# method 2 to create a list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# for x in thislist:
#   print(x)

for i in range(len(thislist)-2):
  print(thislist[i])
  
i=0
while i<len(thislist):
  print(thislist[i])
  i=i+1

newlist = [x for x in range(10) if x < 15]

fruits=["banana",'apple']

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

fruits.sort(reverse=True);
print(fruits)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# x = thisdict.keys()
# x = thisdict.items()
# print(x)

for x, y in thisdict.items():
  print(x, y)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
