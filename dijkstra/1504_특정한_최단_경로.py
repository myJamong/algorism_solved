# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

import sys
from heapq import heappop,heappush
def solve(start):
    q = []
    heappush(q,(0,start))
    costs = [sys.maxsize] * (n+1)
    costs[start] = 0
    while q:
        now_val,now = heappop(q)
        if costs[now] < now_val:
            continue
        for i in graph[now]:
            e,c = i
            if costs[e] <= c or costs[e] <= now_val:
                continue
            if costs[e] > now_val + c:
                costs[e] = now_val + c
                heappush(q,(costs[e],e))
    return costs

if __name__ == "__main__":
    read = sys.stdin.readline
    n,e = map(int,read().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a,b,c = map(int,read().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    v1,v2 = map(int,read().split())
    costs_v1,costs_v2 = solve(v1),solve(v2)
    result = costs_v1[v2] + min(costs_v1[1]+costs_v2[n],costs_v1[n]+costs_v2[1]) # v1 --> v2 + min(1-->v1,v2-->n or 1-->v2,v1-->n)
    print(result if result < sys.maxsize else -1)
