from collections import Counter
n = int(input())
a = map(int,input().split())
m = int(input())
b = map(int,input().split())
c = Counter(a)
for i in b:
    if i in c:
        print(c[i],end=' ')
    else:
        print('0',end=' ')