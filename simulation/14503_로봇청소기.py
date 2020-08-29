# https://www.acmicpc.net/problem/14503
# 로봇 청소기

import sys
def rotate_d(d): # 방향 전환용 함수
    return 3 if d-1 < 0 else d-1

if __name__ == "__main__":
    dh = [-1,0,1,0] # 북, 동, 남, 서
    dw = [0,1,0,-1]
    height,width = map(int,sys.stdin.readline().split())
    h,w,direction = map(int,sys.stdin.readline().split())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(height)]
    cnt = 1
    arr[h][w] = 2 # 벽이랑 구분하기 위해 1이외의 수를 사용
    while True:
        if (arr[h+dh[0]][w+dw[0]] != 0 # 4방향 모두 청소되었거나 벽인 경우
            and arr[h+dh[1]][w+dw[1]] != 0
            and arr[h+dh[2]][w+dw[2]] != 0
            and arr[h+dh[3]][w+dw[3]] != 0):
            if arr[h-dh[direction]][w-dw[direction]] == 1: # 후진시 벽인 경우
                break
            else: # 후진
                h -= dh[direction]
                w -= dw[direction]
        elif arr[h+dh[rotate_d(direction)]][w+dw[rotate_d(direction)]] == 0: # 좌측으로 방향전환 했을 시 청소해야하는 구역인지 확인
            direction = rotate_d(direction) # 방향 전환
            h += dh[direction] # 이동
            w += dw[direction]
            cnt += 1
            arr[h][w] = cnt +1
        else: # 좌측이 청소되었거나 벽인 경우 회전
            direction = rotate_d(direction)
    print(cnt)
