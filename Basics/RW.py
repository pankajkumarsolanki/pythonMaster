with open('../../../../PycharmProjects/pythonProject/testfile.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('../../../../PycharmProjects/pythonProject/testfile.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
            print(line) 


