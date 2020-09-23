# https://www.acmicpc.net/problem/2623
# 음악프로그램 --> 위상정렬 

import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    n,pd = map(int,read().split())
    in_degree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(pd):
        order = list(map(int,read().split()))
        for i in range(2,len(order)):
            in_degree[order[i]] += 1
            graph[order[i-1]].append(order[i])
    q = deque()
    for i in range(1,n+1):
        if in_degree[i] == 0:
            q.append(i)
    res = []
    while q:
        now = q.popleft()
        res.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    if len(res) == n:
        for i in res:
            print(i)
    else:
        print(0)
