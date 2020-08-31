# https://www.acmicpc.net/problem/15683
# 감시

import sys   
def cover(arr,t,y,x,d): 감시 구역 확인
    dirs = [d] # 감시 가능한 방향 담은 배열
    if t in(2,4,5):
        dirs.append(d+2 if d < 2 else d-2)
    if t in (3,4,5):
        dirs.append(d-1 if d > 0 else 3)
    if t == 5:
        dirs.append(d+1 if d < 3 else 0)
    
    if 0 in dirs: # 동쪽 감시
        for j in range(x+1,w):
            if arr[y][j] == 0:
                arr[y][j] = '#'
            elif arr[y][j] == 6:
                break
    if 1 in dirs: # 남쪽 감시
        for i in range(y+1,h):
            if arr[i][x] == 0:
                arr[i][x] = '#'
            elif arr[i][x] == 6:
                break
    if 2 in dirs: # 서쪽 감시
        for j in range(x-1,-1,-1):
            if arr[y][j] == 0:
                arr[y][j] = '#'
            elif arr[y][j] == 6:
                break
    if 3 in dirs: # 북쪽 
        for i in range(y-1,-1,-1):
            if arr[i][x] == 0:
                arr[i][x] = '#'
            elif arr[i][x] == 6:
                break
    
def dfs(l,s): # 깊이 우선 탐색
    global result
    if l == len(cctvs): # 모든 CCTV 방향 확인
        temp = [x.copy() for x in arr]
        for i in range(len(directions)):
            t,y,x = cctvs[i]
            d = directions[i]
            cover(temp,t,y,x,d) # 감시 구역 확인
        cnt = 0
        for i in range(h): # 최소 사각지대 확인
            cnt += temp[i].count(0)
        result = min(result,cnt)
    else: # 방향 확인중
        for i in range(s,len(cctvs)):
            n = 4 # 방향의 갯수
            if cctvs[i][0] == 2:
                n = 2
            elif cctvs[i][0] == 5:
                n = 1
            for j in range(n):
                if directions[i] == -1:
                    directions[i] = j
                    dfs(l+1,i+1)
                    directions[i] = -1

if __name__ == "__main__":
    h,w = map(int,sys.stdin.readline().split())
    cctvs = [] # CCTV용 배열
    arr = [] # 지도용 배열
    result = h*w
    for i in range(h):
        temp = list(map(int,sys.stdin.readline().split()))
        arr.append(temp)
        for j in range(w):
            if arr[i][j] not in (0,6):
                cctvs.append((arr[i][j],i,j)) # CCTV 종류와 좌표 저장
    directions = [-1]*len(cctvs) # 방향 확인용 배열
    dfs(0,0)
    print(result)
