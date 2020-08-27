# https://www.acmicpc.net/problem/11052
# 카드 구매하기

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    arr.insert(0,0)
    dp = [0] * (n+1)
    dp[1] = arr[1]
    for i in range(2,n+1):
        temp = [arr[i]]
        for j in range(1,i):
            temp.append(dp[i-j]+arr[j])
        dp[i] = max(temp)
    print(dp[n])
