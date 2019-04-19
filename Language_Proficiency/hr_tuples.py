

def main():
    n = int(input())
    integer_list = map(int, input().split())
    mytuple = tuple(integer_list)
    print(hash(mytuple))

if __name__ == '__main__':
    main()
