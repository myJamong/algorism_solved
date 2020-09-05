# https://www.acmicpc.net/problem/16940
# 
import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [[] for _ in range(n+1)]
    chk = [0] * (n+1)
    order = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,read().split())
        arr[a].append(b)
        arr[b].append(a)
    res = [0] + list(map(int,read().split()))
    for i in range(1,n+1): # 확인 결과의 순서 저장
        order[res[i]] = i
    for i in arr: # 방문 순서를 확인 결과에 맞게 정렬
        i.sort(key=lambda x:order[x])
    q = deque()
    q.append(1)
    chk[1] = 1
    res.pop(0)
    while q:
        now = q.popleft()
        if now != res.pop(0):
            print(0)
            break
        for i in arr[now]:
            if chk[i] == 0:
                q.append(i)
                chk[i] = 1
    else:
        print(1)
