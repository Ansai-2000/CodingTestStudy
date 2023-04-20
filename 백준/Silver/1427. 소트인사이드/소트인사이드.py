n = input()
a = []
s = ''
for i in n:
    a.append(int(i))
    
a.sort()
a.reverse()
for i in range(len(a)):
    print(a[i],end='')