# https://www.acmicpc.net/problem/2579
# 계단 오르기

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [0] * 301
    for i in range(1,n+1):
        arr[i] = int(sys.stdin.readline())
    dp = [0] * 301
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    dp[3] = max(arr[1]+arr[3],arr[2]+arr[3])
    for i in range(4,n+1):
        dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])
    print(dp[n])      
