print("hello")
a, b, c = 1, 2.2, "myself"
print(a, b, c)
print(a+b)
d = "{} {}".format("value is", b)
print(d)
print(type(d), type(a), type(b), type(c))
mt = [1, 2, "mike", "a"]
print(mt[0], mt[1], mt[2], mt[-1])
print(mt[0:3])
print(mt[1:3])
print(mt[0:4:2])
mt.insert(3, "manage")
print(mt)
mt.append("last")
print(mt)
mt[2] = "changed"
print(mt)
mt[3]= "UPDATED"
print(mt)
del mt[0]
print(mt)
print(type(mt))
# Numeric - int, float, complex
# String - Any Text or Characters
# List - Once declared can be updated | a=[,2,3]
# Tuple - Similar to List, but cannot be updated once declared | a=(1,2,3)
# Dictionary - Key Value Pair Combination (Similar to hashmap in Java) | a={1:"name", 2:"test"}

tup = (1, 2, 3.4, "NAME")
print(tup)
print(tup[0])

dic = {1: "Name", 2: "Value", 3: 2.3, "de": "Mike"}
print(type(dic))
print(dic["de"])

dic1 = {}
dic1["first"] = 1
dic1["middle"] = "middlessss"
print(dic1)
print(dic1["middle"])
