# https://www.acmicpc.net/problem/2231
# 분해합

import sys
def creator(num): # 생성자 구하는 함수
    temp = num
    while num > 0:
        temp += num%10
        num //= 10
    return temp

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    for i in range(num-len(str(num))*9,num+1): # 각 자리에 9 인경우를 뺐을 때가 최소 수
        if creator(i) == num:
            print(i)
            break
    else:
        print(0)
