# https://www.acmicpc.net/problem/2056
# 작업 --> 위상정렬 + DP

import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    in_degree = [0] * (n+1)
    dp = [0] * (n+1)
    times = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        info = list(map(int,read().split()))
        times[i] = info[0]
        for j in range(2,len(info)):
            graph[info[j]].append(i)
            in_degree[i] += 1
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
    print(max(dp)) # 무조건 마지막 번호가 끝이라는 보장 없음 --> 최대 값이 모든 작업이 끝난 시간
