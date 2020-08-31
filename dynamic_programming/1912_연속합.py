# https://www.acmicpc.net/problem/1912
# 연속합

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [0] + list(map(int,read().split()))
    dp = [-1001] * (n+1)
    for i in range(1,n+1):
        # 현재위치 숫자랑 이전까지의 합 중 최대값
        # 이게 중간에 연속되는 값이 최대가 되는 경우를 고려할때
        # --> 양수의 연속이면 그냥 쭉 더하는게 최대값 그래서 중간에 연속되는일이 없음
        # --> 음수가 나오는 경우 중간의 견속되는 경우가 생기는데... 음수 나오다 양수 나올때 여태 합이 현재값보다 작으면 현재값을 시작으로 합 시작함
        dp[i] = max(arr[i],dp[i-1]+arr[i]) 
    print(max(dp))
