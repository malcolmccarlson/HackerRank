def count_substring(string, sub_string):
    count = 0
    sl = len(string)
    ssl = len(sub_string)
    for i in range(0, sl - ssl + 1):
        if string[i:i + ssl] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
