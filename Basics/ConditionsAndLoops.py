# If Condition!
a = 2
if a == 2:
    print("Passed")
    print("WOW")
    print("{} {}".format(a, "Is the Right Value"))
else:
    print("failed")
    print("uh oh")
print("Completed")
print("*********************************************")

# For LOOPS!
sample1 = [1, "Tommy", 3.0, 4.4, 55, 666, 777.77]
for i in sample1:
    print(i)
    print(i * 2)  # Multiplies the values
print("*********************************************")

# Sum of 1st 5 Natural Numbers 1+2+3+4+5 = 15
k = 0
for j in range(0, 6):  # range(i,j) > i to j-1
    print(j)
    k = k + j
print(k)
print("*********************************************")

#
for l in range(1, 10, 3):  # range(i,j) > i to j-1, j+3
    print(l)
for m in range(10, 3):  # Skipping First Index
    print(m)
print("*********************************************")

# While LOOPS!
n = 4
while n < 10:
    print(n)
    n = n + 1
print("*********************************************")

# While LOOPS!
o = 10
while o > 1:
    if o == 9:
        o = o - 1
        continue # Skips only te current Iteration
    if o == 3:
        break # Stops at the Current Iteration
    print(o)
    o = o - 1
