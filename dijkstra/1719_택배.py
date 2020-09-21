# https://www.acmicpc.net/problem/1719
# 택배

import sys
from heapq import heappush,heappop
def solve(start):
    costs = [sys.maxsize] * (n+1)
    costs[start] = 0
    firsts = ['-'] * n # 결과 반환용
    q = []
    heappush(q,(0,start,0)) # 값, 노드, 첫
    while q:
        now_val,now,first = heappop(q)
        for i in graph[now]:
            e,c = i
            if now == start: # 처음 방문하는 집하장
                first = e
            if costs[e] <= now_val or costs[e] <= c:
                continue
            if now_val + c < costs[e]:
                costs[e] = now_val + c
                firsts[e-1] = str(first)
                heappush(q,(costs[e],e,first))
    return firsts

if __name__ == "__main__":
    read = sys.stdin.readline
    n,m = map(int,read().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,c = map(int,read().split())
        graph[s].append((e,c))
        graph[e].append((s,c))
    for i in range(1,n+1):
        print(' '.join(solve(i)))
