# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
# input() 사용시 시간초과 문제로 sys.stdin.readline()을 사용하여 해결

import sys
from collections import deque
if __name__ == "__main__":
    node, line = map(int,sys.stdin.readline().split()) # 정점의 개수
    arr = [[0] * node for _ in range(node)] # 연결 정보
    chk = [0] * node # 방문 확인용
    
    # 연결 정보 입력
    for i in range(line):
        start,end = map(int,sys.stdin.readline().split())
        arr[start-1][end-1] = 1
        arr[end-1][start-1] = 1
    
    q = deque()
    result = 0
    for i in range(node):
        if chk[i] == 0:
            chk[i] = 1
            q.append(i)
            result += 1
            while q:
                now = q.popleft()
                for j in range(node):
                    if arr[now][j] == 1 and chk[j] == 0:
                        q.append(j)
                        chk[j] = 1
    print(result)
