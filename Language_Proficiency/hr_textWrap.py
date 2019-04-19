
def wrap(string, max_width):
    start = 0
    for char in string:
        sObject = slice(start, max_width)
        newstring = string[sObject]
        print(newstring)
        start += 4
        max_width += 4


if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)

