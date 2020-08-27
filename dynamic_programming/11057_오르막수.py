# https://www.acmicpc.net/problem/11057
# 오르막수

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [[0] * 10 for _ in range(n)]
    for i in range(10):
        dp[0][i] = 1
    for i in range(1,n):
        for j in range(10):
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]
    print(sum(dp[n-1])%10007)        
