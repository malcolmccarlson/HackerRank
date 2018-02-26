def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = [int(a0), int(a1), int(a2)]
    b = [int(b0), int(b1), int(b2)]

    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    print(alice, bob)


if __name__ == '__main__':
    solve(5,6,7,3,6,10)