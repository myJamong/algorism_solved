# https://www.acmicpc.net/problem/2252
# 줄세우기 --> 위상정렬 

import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    n,m = map(int,read().split())
    in_degree = [0] * (n+1) # 진입 차수 배열
    graph = {} # 연결 정보
    for _ in range(m):
        a,b = map(int,read().split())
        in_degree[b] += 1
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    q = deque()
    result = []
    for i in range(1,n+1): # 진입차수 없는 출발 지점 확인
        if in_degree[i] == 0:
            q.append(i)
    while q:
        x = q.popleft()
        result.append(x)
        if x in graph:
            for j in graph[x]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    q.append(j)
    print(' '.join(map(str,result)))
