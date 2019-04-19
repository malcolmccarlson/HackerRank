import string

def swap_case(s):
    tmplist = []
    for item in s[:]:
        if item.islower() == True:
            tmplist.append(item.upper())
        else:
            tmplist.append(item.lower())
    newstring = ''.join(tmplist)
    return newstring

if __name__ == '__main__':
    mystring = input()
    print(swap_case(mystring))
