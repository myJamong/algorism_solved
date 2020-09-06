# https://www.acmicpc.net/problem/2146
# 다리만들기

import sys
from collections import deque
sys.setrecursionlimit(10**6) # 재귀 횟수 제한 수정
def dfs(h,w,cnt): # 각 섬의 영역 구하는 함수
    arr[h][w] = cnt
    for k in range(4):
        hh = h + dh[k]
        ww = w + dw[k]
        if 0 <= hh < n and 0 <= ww < n and arr[hh][ww] == 1:
            dfs(hh,ww,cnt)

if __name__ == "__main__":
    dh,dw = [-1,0,1,0],[0,1,0,-1]
    read = sys.stdin.readline
    n = int(read())
    result = []
    arr = [list(map(int,read().split())) for _ in range(n)] # 섬의 확장 용
    chk = [[0]*(n) for _ in range(n)] # 들렸는지 확인 및 거리 측정 용
    cnt = 1
    for i in range(n): # 섬 영역 정하기
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i,j,cnt)
    q = deque()
    for i in range(n): # 각 영역의 시작 부분을 큐에 넣기
        for j in range(n):
            if arr[i][j] > 0:
                q.append((i,j))
                chk[i][j] = 1
    while q:
        h,w = q.popleft()
        for k in range(4):
            hh = h + dh[k]
            ww = w + dw[k]
            if 0 <= hh < n and 0 <= ww < n: # 범위 안에 있는 경우
                if chk[hh][ww] == 0: # 아직 방문하지 않은 경우
                    arr[hh][ww] = arr[h][w] # 섬의 확장
                    chk[hh][ww] = chk[h][w] + 1 # 거리
                    q.append((hh,ww))
                elif arr[hh][ww] != 0 and arr[hh][ww] != arr[h][w]: # 다른 섬에의 확장에 도달한 경우
                    if chk[hh][ww] == 1: # 섬과의 거리가 1인 경우
                        result.append(chk[h][w]-1)
                    elif chk[hh][ww] > 1: # 섬과의 거리가 2 이상인 경우
                        result.append(chk[hh][ww] + chk[h][w] - 2) # 거리 측정은 2부터 시작했기 때문에 각각 섬 - 2
    print(min(result) if result else 0)
