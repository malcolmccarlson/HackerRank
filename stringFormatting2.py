
def formatForNumbers(num):
    width = len('{:b}'.format(num))# max value for binary num
    for i in range(1, num+1): # start at 1, go to num+1
        print(str('{0:d}'.format(i)).rjust(width),
              str('{0:o}'.format(i).rjust(width)),
              str('{0:x}'.format(i)).rjust(width).upper(),
              str('{0:b}'.format(i)).rjust(width)
             )

if __name__ == '__main__':
    n = int(input())
    formatForNumbers(n)
