import string

def print_full_name(a, b):
    first_name = str(a)
    last_name= str(b)
    retstring = "{} {}!".format(first_name, last_name)
    print("Hello", retstring, "You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
