# https://www.acmicpc.net/problem/1003
# 피보나치 함수

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    dp = [[0,0]] * (42)
    dp[0] = [1,0]
    dp[1] = [0,1]
    for i in range(2,42):
        dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
    for _ in range(n):
        print(' '.join(map(str,dp[int(read())])))
