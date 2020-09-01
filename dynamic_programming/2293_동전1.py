# https://www.acmicpc.net/problem/2293
# 동전 1

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n,k = map(int,read().split())
    coins = [int(read()) for _ in range(n)]
    dp = [0] * (k+1)
    dp[0] = 1 # 동전 자기 자신을 위한 count
    for coin in coins:
        for j in range(coin,k+1):
            dp[j] += dp[j-coin] # 여태까지 사용한 동전으로 j를 만들수 있는 방법 dp[j]에다가 현재 동전 하나를 더해서 사용할 수 있는 새로운 방법 dp[j-coin] 더함
    print(dp[k])
