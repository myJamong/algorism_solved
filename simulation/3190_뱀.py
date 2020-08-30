# https://www.acmicpc.net/problem/3190
# 뱀

import sys
from collections import deque
if __name__ == "__main__":
    dh = [0,1,0,-1] # 동, 남, 서, 북
    dw = [1,0,-1,0]
    wall, apple, snake = 1, 2, 3
    n,k = int(sys.stdin.readline()),int(sys.stdin.readline())
    arr = [[wall]*(n+2)] # 보드 배열에 테두리를 1로 표시하여 벽으로 인지
    for i in range(n):
        arr.append([wall] + [0]*n + [wall])
    arr.append([wall]*(n+2))
    for _ in range(k):
        y,x = map(int,sys.stdin.readline().split())
        arr[y][x] = apple
    r = int(sys.stdin.readline())
    time_line = deque()
    for _ in range(r):
        t,d = map(str,sys.stdin.readline().split())
        time_line.append((int(t),d))
    h = w = 1 # 뱀의 머리 좌표
    arr[h][w] = snake
    direction = time = 0
    snake_q = deque() # 뱀의 길이 확인용 큐
    snake_q.append((h,w))
    
    while True:
        time += 1
        hh,ww = h+dh[direction],w+dw[direction] # 이동 방향으로 한칸 이동
        if 1 <= hh <= n and 1 <= ww <= n: # 보드 내에 뱀이 있는지 확인
            if arr[hh][ww] in (0,apple): # 빈공간이거나 사과에 도착했을 때
                snake_q.append((hh,ww))
                if arr[hh][ww] == 0: # 빈 공간인 경우 뱀의 꼬리 부분을 큐에서 제외하여 이동한것처럼 보이게함        
                    h_b,w_b = snake_q.popleft()
                    arr[h_b][w_b] = 0
                h,w = hh,ww
                arr[h][w] = snake
                if time_line and time_line[0][0] == time: # 방향 이동 시간에 도달했을 때
                    if time_line[0][1] == 'D': # 오른쪽으로 방향전환
                        direction = direction+1 if direction+1 < 4 else 0
                    else: # 왼쪽으로 방향전환
                        direction = direction-1 if direction-1 > -1 else 3
                    time_line.popleft()
            else: # 이동 위치가 뱀인 경우
                break
        else: # 보드 밖으로 뱀이 나간 경우
            break
    print(time)    
