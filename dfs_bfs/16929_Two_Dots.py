# https://www.acmicpc.net/problem/16929
# Two Dots
# DFS를 사용하는데 보드의 각각 모든 지점을 시작 위치로 탐색하는 방식으로 chk[][] 값을 DFS탐색 후 다시 0으로 복귀 시켜준다.
# 사이클이 이루어지면 result 값을 True로 바꾸고 DFS 탐색시 바로 탈출

import sys
def dfs(y,x,start_y,start_x,color,cnt):
    global result
    if result: # 이미 만났으면 탈출
        return
    for d in range(4):
        hh = y + dh[d]
        ww = x + dw[d]
        if 0 <= hh < h and 0 <= ww < w: # 보드 범위 안에 들어온 경우
            if arr[hh][ww] == color and chk[hh][ww] == 0: # 사방향 중 이전 위치와 색이 같고 아직 들리지 않는 곳
                chk[hh][ww] = 1
                dfs(hh,ww,start_y,start_x,color,cnt+1)
                chk[hh][ww] = 0
            elif chk[hh][ww] == 1 and start_y == hh and start_x == ww and cnt >= 4: # 이미 들렸고 시작 위치랑 같고 점위 갯수가 4가 넘는 곳 --> 시작에서 다시 만나는 지점
                result = True
                return
    
if __name__ == "__main__":
    dh = [-1,0,1,0]
    dw = [0,1,0,-1]
    read = sys.stdin.readline
    h,w = map(int,read().split())
    arr = [list(read().strip()) for _ in range(h)]
    chk = [[0] * w for _ in range(h)]
    result = False
    for i in range(h):
        for j in range(w):
            if chk[i][j] == 0:
                chk[i][j] = 1
                dfs(i,j,i,j,arr[i][j],1)
                chk[i][j] = 0
    print('Yes' if result else 'No')
