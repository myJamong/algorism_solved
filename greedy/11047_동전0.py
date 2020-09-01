# https://www.acmicpc.net/problem/11047
# 동전0

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n,k = map(int,read().split())
    coins = [int(read()) for _ in range(n)]
    coins.sort(reverse=True)
    result = 0
    for coin in coins:
        cnt = k // coin
        result += cnt
        k %= coin
        if k == 0:
            print(result)
            break
