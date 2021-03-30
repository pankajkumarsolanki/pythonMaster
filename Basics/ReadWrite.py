file = open("../../../../PycharmProjects/pythonProject/testfile.txt")
# print(file.read()) #Reads full file
# print(file.read(4)) #Reads first 4 characters / bytes of the files
# print(file.readline()) #Reads first line of file
# print(file.readline()) #Reads second line of file

#Print line by line all the lines in the file
# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()

#Print line by line using readlines
for line in file.readlines():
    print(line)
file.close()