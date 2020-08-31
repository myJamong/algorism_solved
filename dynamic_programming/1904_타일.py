# https://www.acmicpc.net/problem/1904
# 타일

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [0] * (n+3)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746 # n의 범위가 1,000,000까지 이기 때문에 int범위를 초과하여 메모리 초과가 날 수 있어 for문 안에서 연산을 해준다.
    print(dp[n])        
