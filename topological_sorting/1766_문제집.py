# https://www.acmicpc.net/problem/1766
# 문제집 --> 위상 정렬과 우선순위 큐를 이용한 문제

import sys
from heapq import heappush,heappop
if __name__ == '__main__':
    read = sys.stdin.readline
    n,m = map(int,read().split())
    in_degree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,read().split())
        in_degree[b] += 1
        graph[a].append(b)
    q = []
    for i in range(1,n+1):
        if in_degree[i] == 0:
            heappush(q,i)
    res = []
    while q:
        now = heappop(q)
        res.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heappush(q,i)
    print(' '.join(map(str,res)))
