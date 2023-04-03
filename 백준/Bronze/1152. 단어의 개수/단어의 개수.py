from sys import stdin

s = stdin.readline().split(" ")
a = []
for i in range(len(s)):
    if(s[i] != "" and s[i] != "\n"):
        a.append(s[i])

print(len(a))
