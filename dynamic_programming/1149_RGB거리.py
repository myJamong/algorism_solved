# https://www.acmicpc.net/problem/1149
# RGB거리

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = arr[0]
    for i in range(1,n):
        dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])
    print(min(dp[-1]))
