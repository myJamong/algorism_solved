# https://www.acmicpc.net/problem/14891
# 톱니바퀴

import sys
def gear_stat(): # 톱니바퀴의 극 상태 배열로 반환
    return [
        gears[0][2] == gears[1][6],
        gears[1][2] == gears[2][6],
        gears[2][2] == gears[3][6]
    ]

def gear_rotate(gear_num,direction): # 해당 톱니바퀴 회전
    temp = gears[gear_num]
    if direction == 1:
        temp.insert(0,temp.pop())
    else:
        temp.append(temp.pop(0))
    return temp

if __name__ == "__main__":
    gears = [list(sys.stdin.readline().strip()) for _ in range(4)]
    k = int(sys.stdin.readline())
    rotates = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]
    for move in rotates:
        gear,direction = move
        stat = gear_stat() # 현재 톱니바퀴 상태 받아오기
        change_arr = [(gear-1,direction)] # 회전 시켜야할 톱니바퀴용 배열
        if gear == 1: # 1번 톱니바퀴인 경우 
            for i in range(len(stat)):
                if not stat[i]:
                    direction *= -1
                    change_arr.append((i+1,direction))
                else:
                    break
        elif gear == 2: # 2번 톱니바퀴인 경우 
            if not stat[0]:
                change_arr.append((0,-direction))
            if not stat[1]:
                change_arr.append((2,-direction))
                if not stat[2]:
                    change_arr.append((3,direction))
        elif gear == 3: # 3번 톱니바퀴인 경우 
            if not stat[2]:
                change_arr.append((3,-direction))
            if not stat[1]:
                change_arr.append((1,-direction))
                if not stat[0]:
                    change_arr.append((0,direction))
        else: # 4번 톱니바퀴인 경우 
            for i in range(len(stat),0,-1):
                if not stat[i-1]:
                    direction *= -1
                    change_arr.append((i-1,direction))
                else:
                    break
        for i in change_arr: # 회전 필요한 톱니바퀴 회전
            gear_rotate(i[0],i[1])
    result = 0
    for i in range(4): # 결과 
        if int(gears[i][0]) == 1:
            result += 2**i
    print(result)
