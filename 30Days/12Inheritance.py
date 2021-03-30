class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNum, scores):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores

    def printPerson(self):
        print("Name: {}, {}", format(self.lastName,self.firstName))
        print("ID: {}".format(self.idNum))

    def calculate(self):
        x = len(self.scores)
        n = 0
        for i in range(x):
            n += self.scores[i]

        y = int(n) // int(x)

        if 90 <= y <= 100:
            return 'O'
        elif 80 <= y < 90:
            return 'E'
        elif 70 <= y < 80:
            return 'A'
        elif 55 <= y < 70:
            return 'P'
        elif 40 <= y < 55:
            return 'D'
        else:
            return 'T'