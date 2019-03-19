import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        print(s)
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        # print(L)
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

