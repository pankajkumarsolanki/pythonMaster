
#Create a function that takes in two integers and returns True if their sum is 10, False if their sum is something else
def check_ten(n1,n2):
    if n1+n2 == 10:
        print(True)
    else:
        print(False)
check_ten(10, 0)
check_ten(5,5)
check_ten(2,7)
print("-"*50)


#Create a function that takes in two integers and returns True if their sum is 10, otherwise, return the actual sum value
def check_ten_sum(n1,n2):
    if n1+n2 == 10:
        print(True)
    else:
        print(n1+n2)
check_ten_sum(10,0)
check_ten_sum(2,7)
print("-"*50)

#Create a function that takes in a string and returns back the first character of that string in upper case
def first_upper(mystring):
    print(mystring[0].upper())
first_upper('hello')
first_upper('agent')
print("-"*50)

#Create a function that takes in a string and returns the last two characters. If there are less than two chracters, return the string: "Error"
def last_two(mystring):
    a = len(mystring)
    if a<2:
        print("Error")
    else:
        print(mystring[-2:])

last_two('hello')
last_two('hi')
last_two('a')
print("-"*50)

#Given a list of integers, return True if the sequence [1,2,3] is somewhere in the list. Hint: Use slicing and a for loop.
def seq_check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i + 1]==2 and nums[i + 2]==3:
            print(True)
        

seq_check([1, 2, 3])
seq_check([7,7,7,1,2,3,7,7,7])
seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3])
print("-"*50)

#Given a 2 strings, create a function that returns the difference in length between them. This difference in length should always be a positive number (or just 0). Hint: Absolute Value
def compare_len(s1,s2):
    di = len(s1)-len(s2)
    print(abs(di))

compare_len('aa', 'aa')
compare_len('a','bb')
compare_len('bb','a')
print("-"*50)

#Given a list of integers, if the length of the list is an even number, return the sum of the list. If the length of the list is odd, return the max value in that list
def sum_or_max(mylist):
    if len(mylist)%2==0:
       print(sum(mylist))
    else:
        print(max(mylist))

sum_or_max([1, 2, 3])
sum_or_max([0,1,2,3])
print("-"*50)

#replace
def replace_and_switch(name):
    output = list(name)
    for i, letter in enumerate(name):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i]='x'
    a = output[0]
    b = output[-1]
    output[0]=b
    output[-1]=a
    print(''.join(output))

replace_and_switch('James')
replace_and_switch('Cindy')
replace_and_switch("Alfred")