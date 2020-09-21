# https://www.acmicpc.net/problem/1916
# 최소비용 구하기

import sys
import heapq # 힙을 사용하여 최소비용 산정
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
    costs[start] = 0 # 시작점에서 시작점은 0
    q = []
    heapq.heappush(q,start)
    while q:
        now = heapq.heappop(q)
        for i in graph[now]:
            e,c = i
            if c >= costs[e] or costs[now] >= costs[e]: # 이미 정해진 비용보다 합산중 일부가 큰 경우 그냥 패스
                continue
            if costs[e] > costs[now] + c: 
                costs[e] = costs[now] + c
                heapq.heappush(q,e) # 최소비용으로 갱신되는 부분만 힙에추가 --> 임시적 최소비용
    print(costs[end])    
