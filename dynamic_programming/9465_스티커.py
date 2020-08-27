# https://www.acmicpc.net/problem/9465
# 스티커

import sys
if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        arr = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        for i in range(1,n):
            for j in range(2):
                temp = [dp[1-j][i-1]]
                if i >= 2:
                    temp.append(dp[0][i-2])
                    temp.append(dp[1][i-2])
                dp[j][i] = max(temp) + arr[j][i] if temp else arr[j][i]
        print(max(dp[0][n-1],dp[1][n-1]))
