import string


alpha = string.ascii_lowercase
n = int(input())
somelist= []

for i in range(n):
    s = "-".join(alpha[i:n])
    somelist.append(s[::-1]+s[1:])
width = len(somelist[0])

for i in range(n-1, 0, -1):
    print(somelist[i].center(width, "-"))

for i in range(n):
    print(somelist[i].center(width, "-"))
