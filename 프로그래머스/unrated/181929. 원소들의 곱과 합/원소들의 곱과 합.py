def solution(num_list):
    s = 0
    mul = 1
    for num in num_list:
        mul *= num
        s += num
    if mul < s*s:
        return 1
    else:
        return 0