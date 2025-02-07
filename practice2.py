# String
a = "String"

#quotesInsideQuotes
#We can use quotes inside quotes as long as they dont match the surrounding quotes
a = "This is a 'String'"
print(a)

#Multiline quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Slicing a string
a = "Hello, World"
print(a[2:5])

#Slicing last part of the string
a = "Hello, World"
print(a[2:])

a = "Slicing at the end"
print(a[-6:])

# UpperCase
a = "Hello, World"
#convert string to lowercase
print(a.lower())
#Convert String to uppercase
print(a.upper())
#Removing whitespace from string
print(a.replace(" ", ""))

# Concatenate string and add a space between strings
a = "This"
b = "Is"
c = "Programming"

d = " ".join([a, b, c])
print(d)

# Combining string and number
name = "Abdullah"
age = 28
message = f"My name is {name} and I am {age} years old"
print(message)

# Escape Character and removed white space from start and end of the message
message = "   I have used \"escaped character\" and removed whitespace here   "
removed_whitespace_message = message.strip()
print(removed_whitespace_message)