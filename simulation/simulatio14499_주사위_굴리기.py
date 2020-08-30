# https://www.acmicpc.net/problem/14499
# 주사위 굴리기

import sys
def dice_roll(dice,direction): # 주사위 굴리기 연산
    temp = dice.copy()
    if direction == 1: # 동 회전
        temp[0] = dice[3]
        temp[2] = dice[0]
        temp[3] = dice[5]
        temp[5] = dice[2]
    elif direction == 2: # 서 회전
        temp[0] = dice[2]
        temp[2] = dice[5]
        temp[3] = dice[0]
        temp[5] = dice[3]
    elif direction == 3: # 북 회전
        temp[0] = dice[4]
        temp[1] = dice[0]
        temp[4] = dice[5]
        temp[5] = dice[1]
    else: # 남 회전
        temp[0] = dice[1]
        temp[1] = dice[5]
        temp[4] = dice[0]
        temp[5] = dice[4]
    return temp
    
if __name__ == "__main__":
    dh = [0,0,0,-1,1] # 지도 y 이동용
    dw = [0,1,-1,0,0] # 지도 x 이동용
    height,width,h,w,k = map(int,sys.stdin.readline().split())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(height)]
    rolls = list(map(int,sys.stdin.readline().split()))
    dice = [0] * 6 # 주사위 정보
    for r in rolls:
        if 0 <= w+dw[r] < width and 0 <= h+dh[r] < height: # 주사위 이동시 지도안에 있는지 여부 확인
            h = h+dh[r]
            w = w+dw[r]
            dice = dice_roll(dice,r) # 주사위 회전
            if arr[h][w] != 0: # 현재 주사위 위치의 지도에 숫자가 적혀있는 경우
                dice[5] = arr[h][w] # 바닥면 주사위 숫자를 지도에 복사
                arr[h][w] = 0
            else:
                arr[h][w] = dice[5] # 지도의 숫자를 주사위 바닥면에 복사
            print(dice[0]) # 주사위 윗면 출력
