n = input()
while n != '0':
    a = list(n)
    a = "".join(reversed(a))
    if a == n:
        print("yes")
    else:
        print("no")
    n = input()
