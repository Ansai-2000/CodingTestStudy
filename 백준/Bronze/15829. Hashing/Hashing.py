n = int(input())
k = input()
r = 31
m = 1234567891
s = 0
for i in range(n):
    s += pow(31,i) * (ord(k[i]) - 96)
print(s)    