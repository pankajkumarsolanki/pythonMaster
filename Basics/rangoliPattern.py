import string

n = 3
alpha = string.ascii_lowercase
rangealpha = alpha[0:n]
items = list(range(n))
items = items[:-1]+items[::-1]
for i in items:
    temp = rangealpha[-(i+1):]
    row = temp[::-1]+temp[1:]
    print("-".join(row).center(n*4-3, "-"))
