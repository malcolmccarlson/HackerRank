def makeDoormat(rows, columns):
    design = '.|.'
    for i in range(1, rows, 2):
        current = str(design * i).center(columns, '-')
        print(current)
    
    print('WELCOME'.center(columns, '-'))

    for i in range(rows-2, 0, -2):
        current = str(design * i).center(columns, '-')
        print(current)


if __name__ == '__main__':
    rows, columns = map(int, input().split())
    makeDoormat(rows, columns)
