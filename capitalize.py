import os
import string

def solve(s):
    print(s[:].split())
    for item in s[:].split():
        s = s.replace(item, item.capitalize())
    print(s)


if __name__ == '__main__':
    name = input()
    solve(name)
