# https://www.acmicpc.net/problem/12865
# 평범한 배냥(냅색 알고리즘)

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n,k = map(int,read().split())
    dp = [0] * (k+1)
    for i in range(n):
        w,v = map(int,read().split())
        # 뒤에서 부터 확인하는 이유는 중복 발생을 피하기 위해
        # 앞에서 부터 확인하고 값을 넣어주게 되면 --> 같은 값을 두번 더하는 경우가 생김.
        # 무게가 1이고 가치가 100인 경우 앞에서 넣으면 dp[i-1] 값에 이미 넣은 상태에서 또 넣는 경우가 발생할 수 있음
        for j in range(k,w-1,-1):
            dp[j] = max(dp[j],dp[j-w]+v)
    print(dp[k])
