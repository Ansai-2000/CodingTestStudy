import sys
input = sys.stdin.readline
t = int(input())
s = set()
for i in range(t):
    str = input().split()
    if len(str) == 2:
        a,b = str[0],str[1]
        b = int(b)
        if a == "add":
            s.add(b)
        elif a == "check":
            if b in s:
                print(1)
            else:
                print(0)
        elif a == "remove":
            s.discard(b)
        elif a == "toggle":
            if b in s:
                s.remove(b)
            else:
                s.add(b)    
    else:            
        if str[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
