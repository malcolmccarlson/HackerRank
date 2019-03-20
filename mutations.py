import string


def mutate_string(string, position, character):
    charList = []
    for item in string:
        charList.append(item)
    charList.pop(position)
    charList.insert(position, character)
    return ''.join(charList)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
