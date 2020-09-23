# https://www.acmicpc.net/problem/3665
# 최종 순위
# 진입차수를 앞순서에서 모두 들어오도록 하는 것 그리고 등수가 변한것에 대해 방향 전환하는 것이 포인트

import sys
from collections import deque
if __name__ == "__main__":
    read = input
    T = int(read())
    for _ in range(T):
        n = int(read())
        order = [0] + list(map(int,read().split()))
        m = int(read())
        in_degree = [0] * (n+1)
        graph = [[-1]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                graph[order[i]][order[j]] = 1 # 방향 설정
                in_degree[order[j]] += 1 # 하위 순위에 대해 진입 차수 누적
        for _ in range(m):
            a,b = map(int,read().split())
            # 등수 변경에 대한 방향 전환
            graph[a][b] *= -1 
            graph[b][a] *= -1
            
            # 무조건 앞 숫자가 우선 등수라는 보장이 없음
            # 순서가 변경되면 진입차수의 수정이 필요함
            if graph[a][b] == 1:
                in_degree[b] += 1
                in_degree[a] -= 1
            else:
                in_degree[a] += 1
                in_degree[b] -= 1
        q = deque()
        for i in range(1,n+1): # 첫번째 찾기
            if in_degree[i] == 0:
                q.append(i)
        res = []
        while q:
            now = q.popleft()
            res.append(now)
            for i in range(1,n+1):
                if graph[now][i] == 1: # 방향 확인
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        q.append(i)
        if len(res) == n:
            print(' '.join(map(str,res)))
        else:
            print('IMPOSSIBLE')
