# https://www.acmicpc.net/problem/1238
# 파티

import sys
from heapq import heappush,heappop
def solve(start,costs,graph):
    q = []
    costs[start] = 0
    heappush(q,(0,start))
    while q:
        now_val,now = heappop(q)
        for i in graph[now]:
            e,c = i
            if costs[e] <= c or costs[e] <= now_val:
                continue
            if now_val + c < costs[e]:
                costs[e] = now_val + c
                heappush(q,(costs[e],e))
    return costs
    
if __name__ == "__main__":
    read = sys.stdin.readline
    n,m,x = map(int,read().split())
    graph_1 = [[]*(n+1) for _ in range(n+1)] # 출발용
    graph_2 = [[]*(n+1) for _ in range(n+1)] # 파티로 돌아가는 용
    costs_1 = [sys.maxsize] * (n+1) # 단방향으로 돌아갈때 값을 저장
    costs_2 = [sys.maxsize] * (n+1) # 출발할때 값을 저장
    totals = [0] * (n+1)
    for _ in range(m):
        s,e,c = map(int,read().split())
        graph_1[s].append((e,c))
        graph_2[e].append((s,c))
    costs_1 = solve(x,costs_1,graph_1)
    costs_2 = solve(x,costs_2,graph_2)
    for i in range(1,n+1):
        totals[i] = costs_1[i] + costs_2[i]
    print(max(totals))
