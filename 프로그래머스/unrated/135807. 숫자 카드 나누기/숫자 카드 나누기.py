import math
def solution(arrayA, arrayB):
    answer = 0
    a = listgcd(arrayA)
    b = listgcd(arrayB)
    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:
            b = 0
            break
    for i in range(len(arrayB)):
        if arrayB[i] % a == 0:
            a = 0
            break
    return max(a,b)

def listgcd(array):
    g = array[0]
    for a in array:
        g = math.gcd(a,g)
    return g    