# https://www.acmicpc.net/problem/2293
# 동전 1

import sys
if __name__ == "__main__":
    n,k = map(int,sys.stdin.readline().split())
    dp = [0] * (k+1)
    dp[0] = 1
    for i in range(n):
        val = int(sys.stdin.readline())
        for j in range(val,k+1):
            if j - val >= 0:
                dp[j] += dp[j-val]
    print(dp[k])
