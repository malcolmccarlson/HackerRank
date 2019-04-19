#!/bin/python3

import sys

# Task
# Given an array, A, of N integers, print A's elements in
# reverse order as a single line of space-separated numbers.

# Input Format
# The first line contains an integer, N(the size of our array).
# The second line contains N space-separated integers describing array A's elements.


n = int(input('Enter an integer for array size.').strip())
arr = [int(arr_temp) for arr_temp in input('Enter integers for array').strip().split(' ')]
print(" ".join(map(str, arr[::-1])))