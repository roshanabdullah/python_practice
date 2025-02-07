#Print Message based on wether the value is true or false
a = 10
b = 100

if a > 100:
    print("A is greater than 100")
else:
    print("A is less than 100")

# bool() function
a = 20
print(bool(a))
b = ""
print(bool(b))
c = 0 
print(bool(c))

a = None
print(bool(a))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

def myFunc():
    return False
if myFunc() is True:
    print("yes")
else:
    print("no")

# Check if value is int or not
a = 100.0
print(isinstance(a, int))