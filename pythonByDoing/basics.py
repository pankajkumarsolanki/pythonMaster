# # for _ in range(int(input())):
# #     x, a, z, b = input(), set(input().split()), input(), set(input().split())
# # print(a.issubset(b))
#
# import random
#
# # This line creates a set with 6 random numbers
# lottery_numbers = set(random.sample(range(22), 6))
#
# # Here are your players; find out who has the most numbers matching lottery_numbers!
# players = [
#     {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
#     {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
#     {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
#     {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
# ]
#

# def over_age(data, getter):
#     return getter(data) >= 18
#
#
# user = {'username': 'rolf123', 'age': '35'}
#
# print(lambda x: int(x['age']))
# print(over_age(user, lambda x: int(x['age'])))

# n, x = map(int, input().split())
#
# sheet = []
# for _ in range(x):
#     sheet.append( map(float, input().split()) )
# print(list(sheet))
# for i in zip(*sheet):
#     print( sum(i)/len(i) )

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
# def solve(meal_cost, tip_percent, tax_percent):
#     tip = (meal_cost * tip_percent)/100
#     tax = (meal_cost * tax_percent) / 100
#     total_cost = meal_cost + tip + tax
#     print(round(total_cost))
#
#
#
# if __name__ == '__main__':
#     meal_cost = 12.00
#     tip_percent = 20
#     tax_percent = 8
#
#     solve(meal_cost, tip_percent, tax_percent)


#
# n = 21
#
# if n%2 != 0 or (n%2==0 and n in range(6,20)):
#     print("Weird")
# else:
#     print("Not Weird")

#
# n = int(input())
# a=[]
# for i in range(n):
#     k = list(input().split())
#     if k[0] == "append" or k[0]== "remove" or k[0]== "insert":
#        eval("{}.{}{}".format("a",k[0],tuple(k[1:])))
#     else:
#         print(k[0])
# print(a)


# class Person:
#     def __init__(self, initialAge):
#         self.age = initialAge
#         if self.age < 0:
#             print("Age is not valid, setting age to 0.")
#             self.age = 0
#
#     def amIOld(self):
#         if self.age < 13:
#             print("You are young.")
#         elif self.age >= 13 and self.age < 18:
#             print("You are a teenager.")
#         else:
#             print("You are old.")
#
#     def yearPasses(self):
#         self.age += 1



# def fibonacci(n):
#     n1 = 0
#     n2 = 1
#     count = 0
#     while count < n:
#         print(n1)
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1
#
# fibonacci(5)
# print("----------------")
# fibonacci(10)

# n = int(input())
# a = []
# for _ in range(0,n):
#     a.append(input())
#
# for x in range(0,len(a)):
#     print("{} {}".format(a[x][0::2],a[x][1::2]))


#
# i = 17
#
# for n in range(1,i+1):
#     print("{} {} {} {}".format(n, oct(n)[2:], hex(n)[2:].upper(), bin(n)[2:]))

# print (min(a.values()))
#
# a["mary"]=20
#
# print(a)
# print (min(a.values()))
#
#
# b= sorted(a.values(),reverse=True)
# c =b[-2]
# 
# n = int(input())
# listOfScore={}
# for i in range(0,n):
#     name = str(input())
#     score = float(input())
#     listOfScore[name]=score
# sortedList = list(set(sorted(listOfScore.values(),reverse=True)))
# print(sortedList)
# secondLeast = sortedList[-2]
# 
# for a,b in sorted(listOfScore.items()):
#     if b==secondLeast:
#         print(a)
# 
# 
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
#
# n = int(input())
#
# nn = {}
# for n in range(0,n):
#     a,b = input().split()
#     nn[a]=b
#
# while True:
#     try:
#         k = input()
#         if k in nn.keys():
#             print("{}={}".format(k,nn[k]))
#         else:
#             print("Not found")
#     except:
#         break
#
# n = 125
# a= len(max(bin(n)[2:].split("0")))
# print(a)

# x, y = map(int,input().split())
# print(y==eval(input()))

# n = int(input())
# width = len("{0:b}".format(n))
# for i in range(1,n+1):
#   print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


# n = int(input())
# a,b = map(int,input().split())
#
# for _ in range(n):
# try:
#
#     print (a/b)
# except ZeroDivisionError as e:
#     print ("Error Code:",e)
#
#
# for i in range(int(input())):

# def count_from_zero_to_n(n):
#     if n > 0:
#         for x in range(0, n+1):
#             print(x)
#     else:
#         raise ValueError("Test")
#
# count_from_zero_to_n(-5)

def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))     # turn the user input into an integer
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print out the message '{user_input} is {even/odd}.'
        except ValueError:
            print("Please input integers only.")
        finally:
            user_input = input('Do you want to play again? (y/n):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit

interact()