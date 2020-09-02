# https://www.acmicpc.net/problem/13023
# ABCDE

import sys
def dfs(l,idx):
    global result
    chk[idx] = 1
    if l >= 4: # 이어져 있는 친구가 4 이상 인경우
        result = 1
    else:
        for i in arr[idx]:
            if chk[i] == 0:
                dfs(l+1,i)
                chk[i] = 0 다른 분기에서 들릴 수 있게 해제
        
if __name__ == "__main__":
    read = sys.stdin.readline
    n,m = map(int,read().split())
    arr = [[] for _ in range(n)] # 시간 초과 발생은로 기존에 했던 0으로 다 채우지 않고 연결 부분만 넣는다.
    chk = [0] * n
    result = 0
    for _ in range(m):
        a,b = map(int,read().split())
        arr[a].append(b)
        arr[b].append(a)
        
    for i in range(n):
        dfs(0,i)
        chk[i] = 0 # 다른 분기에서 들릴수 있게 해제
        if result == 1:
            break
    print(result)
