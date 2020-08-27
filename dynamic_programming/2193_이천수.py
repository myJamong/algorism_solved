# https://www.acmicpc.net/problem/2193
# 이천수

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [0] * (n+2)
    dp[1] = dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
