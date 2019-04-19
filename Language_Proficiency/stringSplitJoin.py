import string


def split_and_join(line):
    tmp = line.split(' ')
    tmp = '-'.join(tmp)
    return tmp

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
