# https://www.acmicpc.net/problem/2565
# 전깃줄

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [[0,0]] + [list(map(int,read().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0]) # A를 기준으로 정렬 --> B에서 증가하는 가장 긴 부분 수열을 찾기 위해
    dp = [0] * (n+2)
    dp[1] = 1
    for i in range(2,n+1):
        temp = []
        for j in range(1,i):
            if arr[j][1] < arr[i][1]:
                temp.append(dp[j])
        dp[i] = max(temp)+1 if temp else 1
    print(n-max(dp)) # 전체에서 가장 긴 증가하는 부분 수열의 길이를 빼주면 정답
