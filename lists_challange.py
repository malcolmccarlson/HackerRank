
def listSort(somelist):
    n = len(somelist)
    for i in range(n):
        for j in range(0, n-i-1):
            if somelist[j] > somelist[j+1]:
                somelist[j], somelist[j+1] = somelist[j+1], somelist[j]
    return somelist

CHOICEDICT = {'insert': lambda somelist, position, element: somelist.insert(position, element),
               'remove': lambda somelist, element: somelist.remove(element),
               'append': lambda somelist, element: somelist.append(element),
               'pop': lambda somelist: somelist.pop(len(somelist)-1),
               'sort': lambda somelist: listSort(somelist),
               'reverse': lambda somelist: somelist.reverse()
              }

def main():
    mylist = []
    printque = []
    N = int(input())
    for i in range(N):
        operation = list(input().split())
        if operation[0] == 'insert':
            CHOICEDICT['insert'](mylist, int(operation[1]), int(operation[2]))
        elif operation[0] == 'remove':
            CHOICEDICT['remove'](mylist, int(operation[1]))
        elif operation[0] == 'append':
            CHOICEDICT['append'](mylist, int(operation[1]))
        elif operation[0] == 'pop':
            CHOICEDICT['pop'](mylist)
        elif operation[0] ==  'sort':
            CHOICEDICT['sort'](mylist)
        elif operation[0] == 'reverse':
            CHOICEDICT['reverse'](mylist)
        elif operation[0] == 'print':
            tmplist = mylist.copy()
            printque.append(tmplist)
        else:
            print("Error")
    for i in printque:
        print(i)

if __name__ == '__main__':
    main()
