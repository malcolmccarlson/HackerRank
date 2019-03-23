

def stringValidator(s):
    print(any(item.isalnum() for item in s))
    print(any(item.isalpha() for item in s))
    print(any(item.isdigit() for item in s))
    print(any(item.islower() for item in s))
    print(any(item.isupper() for item in s))

if __name__ == '__main__':
    s = input()
    stringValidator(s)

