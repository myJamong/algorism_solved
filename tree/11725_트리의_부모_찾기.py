# 
# 트리의 부모 찾기

import sys
from collections import deque
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [[]*(n+1) for _ in range(n+1)]
    chk = [0] * (n+1)
    parent = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,read().split()) 
        arr[a].append(b)
        arr[b].append(a)
    q = deque()
    q.append(1) # 1번이 루트
    while q: # 위에서 부터 아래로 BFS 부모 지정
        now = q.popleft()
        for i in arr[now]:
            if chk[i] == 0:
                chk[i] = 1
                q.append(i)
                parent[i] = now
    for i in range(2,n+1): #출력
        print(parent[i])
