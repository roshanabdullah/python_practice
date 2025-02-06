# Printing Value
print("Hello World!")

# This is a comment

# Variables
a = "string"
b = 5
print(a, b)

#Casting
x = str(3)
y = int(3)
z = float(3)
print(z)
# Getting the type
print(type(z))

# Multiple values, multiple variables
x, y, z = 1, 2, 3
print(x, y, z)

x = y = z = "Orange"
print(x, y, z)

#Unpack values
fruits = ["apple", "banana", "grapes"]
x, y, z = fruits
print(x, y, z)

#Concatenate String
x = "Python"
y = "Is"
z = "Awesome"
print(x + y + z)

# Global Variables
x = "awesome"
def func():
    print("Python is " + x)
func()

# global keyword
def func():
    global x
    x = "Awesome"

func()
print("Python is " + x)




