def solution(n):
    answer = 0
    dp = [0] * 5001
    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    dp[4] = 11
    if n<6:
        return dp[n]
    for i in range(6,n+1,2):
        dp[i] = dp[i-2] * 3 + 2*sum(dp[2:i-2]) + 2
        dp[i] = dp[i] % 1000000007
        
    return dp[i]