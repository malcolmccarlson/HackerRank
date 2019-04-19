#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    newstring = ''
    a_cntr = 0
    for i in range(n):
        newstring += str(s)
        if len(newstring) < n:
            continue
        else:
            break
    newlist = list(newstring)
    diff = len(newlist) - n
    
    for i in range(diff):
        newlist.pop()

    for i in newlist:
        if i == 'a':
            a_cntr += 1
        
    print(a_cntr)

def repeatedString2(s, n):
    a_cntr = s.count('a')
    num = n//len(s)
    mod = n%len(s)
    count = a_cntr*num + s[:mod].count('a')
    return count

    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    # fptr.write(str(result) + '\n')

    # fptr.closeE 
