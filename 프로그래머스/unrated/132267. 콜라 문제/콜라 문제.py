def solution(a, b, n):
    sum = 0
    while(n//a!=0):
        sum += n//a*b
        n = n//a*b + n%a
    return sum    