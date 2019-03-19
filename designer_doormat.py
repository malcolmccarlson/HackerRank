
BAR = '|'
DOT = '.'
DASH = '-'

def takeInfo():
    n, m = input().split()
    return int(n), int(m)

def patternFun(width, mid_point, choice=None):
    if choice == 1:
        print(BAR * width)
    elif choice == 2:
        print(DOT * width)
    elif choice == 3:
        for i in range(width):
            if i%2 == 0:
                print(DASH, end='')
            elif i%2 !=0:
                print(BAR, end='')
            else:
                print('\n')
    else:
        print(DASH * width)

def makeDoormat(height,width):
    mid_point = (int(width/2)-3)
    mid = int(height/2)
    offset = mid_point - 1
    for i in range(height-1):
        if i == mid:
            print(DASH * offset,'WELCOME', DASH * offset)
        patternFun(width, mid_point, 1)

def main():
    n,m = takeInfo()
    makeDoormat(n,m) 

if __name__ == '__main__':
    main()
