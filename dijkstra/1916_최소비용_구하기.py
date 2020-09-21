# https://www.acmicpc.net/problem/1916
# 최소비용 구하기

import sys
import heapq
if __name__ == "__main__":
    INF = sys.maxsize
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    graph = [[] * (n+1) for _ in range(n+1)]
    costs = [INF]*(n+1)
    for _ in range(m):
        s,e,c = map(int,read().split())
        graph[s].append((e,c))
    start,end = map(int,read().split())
    costs[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        now_val,now = heapq.heappop(q)
        if end == now: # heapq 를 사용하는 이유 --> 최소거리기준으로 넣기 때문에 도착 지점을 만나면 바로 break
            break
        for i in graph[now]:
            e,c = i
            if c >= costs[e] or now_val >= costs[e]:
                continue
            if costs[e] > now_val + c:
                costs[e] = now_val + c
                heapq.heappush(q,(costs[e],e))
    print(costs[end])     
