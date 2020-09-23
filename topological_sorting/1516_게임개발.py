# https://www.acmicpc.net/problem/1516
# 게임 개발 --> 위성정렬이랑 DP 같이 사용

import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    times = [0] * (n+1)
    in_degree = [0] * (n+1)
    dp = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        info = list(map(int,read().split()))
        times[i] = info[0]
        for j in range(1,len(info)-1):
            in_degree[i] += 1
            graph[info[j]].append(i)
    q = deque()
    for i in range(1,n+1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = times[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
            dp[i] = max(dp[i],dp[now]+times[i])
    for i in dp[1:]:
        print(i)
