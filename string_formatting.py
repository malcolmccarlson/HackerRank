
def formatString(myint):
    width = len('{:b}'.format(myint))
    for i in range(1,myint+1):
        print(str.rjust(str(i),width), str.rjust(str(oct(i)[2:]),width),
              str.rjust(str(hex(i)[2:]).upper(),width), str.rjust(str(bin(i)[2:]),width))


if __name__ == '__main__':
    int_input = int(input())
    formatString(int_input)

