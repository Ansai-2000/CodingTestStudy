def solution(myString):
    answer = []
    arr = myString.split('x')
    while arr.count("") > 0:
    	arr.remove("")
    arr.sort()
    return arr