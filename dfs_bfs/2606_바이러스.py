# https://www.acmicpc.net/problem/2606
# 바이러스
from collections import deque
if __name__ == "__main__":
    node = int(input()) # 컴퓨터 수
    line = int(input()) # 간선 수
    arr = [[0]*node for _ in range(node)] # 컴퓨터 연결 정보
    chk = [0]*node # 방문 확인용
    
    # 컴퓨터 연결 정보용 입력
    for i in range(line):
        x,y = map(int,input().split())
        arr[x-1][y-1] = 1
        arr[y-1][x-1] = 1
        
    # 1번 컴퓨터의 바이러스
    q = deque()
    q.append(0)
    chk[0] = 1
    result = 0
    
    # BFS 처리
    while q:
        now = q.popleft()
        for i in range(node):
            if arr[now][i] == 1 and chk[i] == 0:
                chk[i] = 1
                q.append(i)
                result += 1
    print(result)
