# https://www.acmicpc.net/problem/9251
# LCS

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    word1,word2 = read().strip(),read().strip()
    h,w = len(word1),len(word2)
    dp = [[0] * (w+1) for _ in range(h+1)] # 확인용 2차원 배열
    for i in range(1,h+1):
        for j in range(1,w+1):
            if word2[j-1] == word1[i-1]: # 비교하는 문자가 같은 경우
                dp[i][j] = dp[i-1][j-1]+1 # 이전 비교회차에서 이전 문자까지 최대값에서 +1
            else: # 문자가 틀릴경우
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) # 이전 비교회차 and 이전 문자 비교 중 최대값 사용
    print(dp[h][w])
