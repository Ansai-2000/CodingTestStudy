def solution(n, m):
    a = n
    b = m
    if(n<m):
        n,m=m,n
    while(n%m!=0):
       	n,m = m,n%m        
    return [m,a*b/m]