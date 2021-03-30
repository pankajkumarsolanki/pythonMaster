ItemsInCart = 0

if ItemsInCart != 2:
    pass
    # raise Exception("ERROR FAILED EXCEPTION")

assert (ItemsInCart == 0)

# -------------------------try/except

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("filenotfound in try catch") #custom exception



try:
    with open('testfilefa.txt', 'r') as reader:
        reader.read()

except Exception as e:
    d= "{} {}".format("python exception is:", e)
    print(d)

finally:
    print("finally block")