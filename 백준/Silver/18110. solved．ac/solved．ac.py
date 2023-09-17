import sys
input = sys.stdin.readline
def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))
arr.sort()
n = round2(t*0.15)
arr = arr[n:len(arr)-n]

s = sum(arr)
if t :
    print(round2(s/len(arr)))
else:
    print(0)    