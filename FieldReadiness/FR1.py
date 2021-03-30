import random

mystring = "Secret agents are super good at staying hidden."

a = mystring.split()
l = [a[i][0] for i in range(0, len(a))]
print(l)

even = [i for i in range(0,11) if i%2==0]
print(even)

for _ in range(0,10):
    print (random.randint(0,11))


for i, letter in enumerate("hello"):
    for j in ["a","e","i","o","u"]:
        if letter[i] == j:
            letter[i] = 'x'
print (letter)