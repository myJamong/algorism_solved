# https://www.acmicpc.net/problem/16940
# BFS 스페셜 저지

import sys
from collections import deque
def bfs():
    if result[0] == 1: # 마지막 입력에서 1로 시작해야 하는 것이 조건
        q = deque()
        q.append(1) # 무조건 첫번째 노드부터 시작
        chk[1] = 1
        result_idx = 1    
        while result_idx < n: # 확인 입력에 마지막 까지 확인 한다.
            now = q.popleft()
            childs = []
            for i in arr[now]:
                if chk[i] == 0:
                    childs.append(i) # 자식 노드 담기
            for i in range(result_idx,result_idx + len(childs)): # BFS이므로 자식 노드가 순서에 상관없이 나열되어 나와야함
                if result[i] in childs: # 입력의 각각 위치에 자식 노드의 순서인지 확인
                    chk[result[i]] = 1 # 해당 노드는 해결 다시 오지 못하게 체크
                    q.append(result[i])
                else: # 자식 노드가 아닌 노드가 오는 경우 BFS가 아님
                    return 0
            result_idx += len(childs)
        return 1
    else: # 마지막 확인 입력에서 시작이 1이 아닌 경우 올바르지 않은 BFS
        return 0
    
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [[] for _ in range(n+1)]
    chk = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int,read().split())
        arr[a].append(b)
        arr[b].append(a)
    result = list(map(int,read().split()))
    print(bfs())
