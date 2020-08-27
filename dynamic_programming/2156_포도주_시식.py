# https://www.acmicpc.net/problem/2156
# 포도주 시식

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [0] + [int(sys.stdin.readline()) for _ in range(n)]
    dp = [0] * (n+2)
    dp[1] = arr[1]
    if len(arr) > 2:
        dp[2] = arr[1] + arr[2]
        for i in range(3,n+1):
            dp[i] = max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])
    print(dp[n])
