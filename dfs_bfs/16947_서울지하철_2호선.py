# https://www.acmicpc.net/problem/16947
# 서울 지하철 2호선

import sys
from collections import deque
sys.setrecursionlimit(10**6) # python3 재귀의 제한이 기본 1000으로 되어있다. 1000회 넘어가면 에러가 발생하므로 수정 필요함
def dfs(curr,prev): # 순환선에 존재하는 역 구하는 함수
    if chk[curr] == 0: # 첫 방문인 경우
        chk[curr] = 1
        for i in lines[curr]: # 해당 역에서 갈 수 있는 역
            if i == prev: # 이전 역이랑 가려는 역이 같은 경우 continue
                continue
            res = dfs(i,curr) # 재귀 진행
            if res > 0: # 방문한 적있지만 이전 역이 아닌 돌아서 역을 만난 경우 이 if 문으로 들어가도록 유도
                chk[curr] = 2 #순환선에 존재하는 역은 2로 표시
                if curr != res: # 순환 시작점 기준으로 잡은 res와 현재 역이 다른 경우 순환 시작점을 반환
                    return res
                else: # 순환 시작점을 만났을때 -1을 반환해서 더이상 순환선에 있는 역은 없는 것으로 판단
                    return -1
    else: # 한번 방문 했지만 바로 이전 역이 아닌 순환해서 만난 역
        return curr # 이 경우 해당 역까지 재귀함수를 빠져나올 것 임으로 현재 값 반환
    return -1

def bfs(curr): # 지선에 있는 역과 순환선의 거리 계산 함수
    q = deque()
    q.append(curr)
    while q:
        now = q.popleft()
        for i in lines[now]:
            if result[i] == -1:
                q.append(i)
                result[i] = result[now] + 1

if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    lines = [[] for _ in range(n+1)]
    for _ in range(n):
        a,b = map(int,read().split())
        lines[a].append(b)
        lines[b].append(a)
    chk = [0] * (n+1)
    dfs(1,0)
    result = [-1] * (n + 1)
    points = []
    for i in range(1,n+1):
        if chk[i] == 2: 
            result[i] = 0
            if len(lines[i]) > 2: # 지선과 만나는 순환선에 존재하는 역
                points.append(i)
    for i in points:
        bfs(i)
    print(' '.join(map(str,result[1:])))
