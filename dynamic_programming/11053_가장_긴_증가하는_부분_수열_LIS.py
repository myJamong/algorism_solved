# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열 LIS

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    arr.insert(0,0)
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2,n+1):
        temp = []
        for j in range(1,i):
            if arr[j] < arr[i]:
                temp.append(dp[j])
        dp[i] = max(temp) + 1 if temp else 1
    print(max(dp))
