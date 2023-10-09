import sys
input = sys.stdin.readline
s = input()
cnt1 = 0
cnt2 = 0
for i in range(len(s)-1):
    if s[i] == '1' and s[i] != s[i+1]:
        cnt1 += 1
    if s[i] == '0' and s[i] != s[i+1]:
        cnt2 += 1

print(min(cnt1,cnt2))