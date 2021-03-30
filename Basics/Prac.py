# If
# is odd, print Weird
# If
# is even and in the inclusive range of to
# , print Not Weird
# If
# is even and in the inclusive range of to
# , print Weird
# If
# is even and greater than , print Not Weird


# !/bin/python

import math
import os
import pdb
import random
import re
import sys
#
# n = 24
#
# if n % 2 == 0:
#     if n in range(2,6):
#         print("Not Weird")
#
#     elif n in range(6,21):
#         print("Weird")
#
#     elif n > 20:
#         print("Not Weird")
# else:
#     print("Weird")
#
# originalMessage = "hello"
# print(originalMessage)
# for i in originalMessage:
#     print(random.sample(originalMessage,1))[0]



n = 5
for i in range(1,n):
    print(i * (10 ** i - 1) // 9)


