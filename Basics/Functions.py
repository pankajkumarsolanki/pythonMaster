# Function is a group of related statements that perform a specific task

def greetme():
    a = 5
    b = a + 5;
    return b


print(greetme())


# ----------------------------------------------------------

def welcome(name):
    print("Good Morning" + name)


welcome("PKS")


# ----------------------------------------------------------

def AddIntegers(a, b):
    c = a + b
    print(c)


AddIntegers(4, 5)

# ----------------------------------------------------------

def AddIntegers2(a, b):
    c = a + b
    return c

print(AddIntegers2(4, 11))