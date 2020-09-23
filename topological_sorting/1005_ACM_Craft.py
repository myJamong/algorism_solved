# https://www.acmicpc.net/problem/1005
# ACM Craft 위상정렬과 DP를 함께사용하는 문제

import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        n,k = map(int,read().split())
        d = [0] + list(map(int,read().split()))
        graph = {}
        in_degree = [0] * (n+1)
        dp = [0] * (n+1)
        for _ in range(k): 
            x,y = map(int,read().split())
            in_degree[y] += 1 #진입 차수 지정
            if x in graph: # 연결정보 입력
                graph[x].append(y)
            else:
                graph[x] = [y]
        q = deque()
        for i in range(1,n+1):
            if in_degree[i] == 0:
                q.append(i)
                dp[i] = d[i]
        while q:
            now = q.popleft()
            if now in graph:
                for j in graph[now]:
                    in_degree[j] -= 1
                    dp[j] = max(dp[j],dp[now]+d[j]) # DP 확인 건설 순서에 두가지 이상 조건이 필요한 경우 최대로 걸리는 시간 이후 건설 시작가능
                    if in_degree[j] == 0:
                        q.append(j)
        print(dp[int(read())])
