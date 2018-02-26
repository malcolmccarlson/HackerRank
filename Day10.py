def dec_to_bin(x):
    stack = [0]
    counter = 0
    binary_num = '{0:08b}'.format(x)
    length = len(binary_num) - 1
    for index, character in enumerate(binary_num):
        if character == "1":
            counter += 1
        if character == '0' or index == length:
            if stack[-1] < counter:
                stack.append(counter)
                counter = 0
    return stack.pop()

def bincount(num):
    result = 0
    maximum = 0

    while num > 0:
        if num % 2 == 1:
            result += 1
            if result > maximum:
                maximum = result

        else:
            result = 0

        num //= 2

    return maximum

def func(num):
  return max(map(len, bin(num)[2:].split('0')))

if __name__ == '__main__':
    print(func(13))
    print(func(13))
    print(bincount(13))