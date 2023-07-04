def solution(a, b):
    arr = [0,31,29,31,30,31,30,31,31,30,31,30]
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if(i == a-1):
            break
    sum += b        
    answer = day[sum % 7]
    
    return answer