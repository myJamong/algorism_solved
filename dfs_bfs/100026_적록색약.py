# https://www.acmicpc.net/problem/10026
# 적록색약
# 일반용 & 적록색약용 배열 정보를 만들어서 BFS를 각각 두번 돌려야한다.
dx = [0,1,0,-1]
dy = [-1,0,1,0]
from collections import deque
def bfs(array,x,y,val):
    q = deque()
    q.append((x,y))
    while q:
        now = q.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                if array[xx][yy] == val:
                    array[xx][yy] = 0
                    q.append((xx,yy))

if __name__ == "__main__":
    n = int(input())
    arr1 = [list(input()) for _ in range(n)]
    arr2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == 'R' or arr1[i][j] == 'G':
                arr2[i][j] = 1
            else:
                arr2[i][j] = 2
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        for j in range(n):
            if arr1[i][j] != 0:
                cnt1 += 1
                bfs(arr1,i,j,arr1[i][j])
            if arr2[i][j] != 0:
                cnt2 += 1
                bfs(arr2,i,j,arr2[i][j])
    print(cnt1,cnt2)
