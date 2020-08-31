# https://www.acmicpc.net/problem/9461
# 파도반 수열

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    dp = [0,1,1,1,2,2,3,4,5]
    for i in range(9,101):
        dp.append(dp[i-1]+dp[i-5]) # 패턴
    for _ in range(int(read())):
        print(dp[int(read())])        
