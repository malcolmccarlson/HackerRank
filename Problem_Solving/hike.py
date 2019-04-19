


def countingValleys(n, s):
    sl = 0
    v = 0
    for step in s:
        if step == 'U':
            sl += 1
        else:
            sl -= 1
        if step == 'U' and sl == 0:
            v += 1
    return v

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
