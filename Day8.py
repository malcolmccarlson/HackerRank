n = int(input())

phonebook = {}

for i in range(0, n):
    kvpair = str(input()).split(' ')
    name = kvpair[0]
    pnum = int(kvpair[1])
    phonebook[name] = pnum

for j in range(0, n):
    name = str(input())
    if name in phonebook:
        phone = phonebook[name]
        print(name + '=' + str(phone))
    else:
        print('Not found')