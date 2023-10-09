import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
m = arr[n-1]
answer = 0
for i in range(n-2,-1,-1):
    if m <= arr[i]:
        answer += arr[i] - m + 1
        arr[i] = m-1
    m = arr[i]
print(answer)