# https://www.acmicpc.net/problem/1167
# 트리의 지름

import sys
def dfs(node,total): # 트리 탐색
    global result
    global start_node
    if result < total:
        result = total
        start_node = node
    for nxt,dist in tree[node]:
        if chk[nxt] == 0:
            chk[nxt] = 1
            dfs(nxt,total+dist)
    
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    chk = [0] * (n+1)
    tree = {}
    result = start_node = 0
    for _ in range(n): # 트리 생성
        line = list(map(int,read().split()))
        tree[line[0]] = [(line[i],line[i+1]) for i in range(1,len(line)-1,2)]
    chk[1] = 1
    dfs(1,0) # start_node를 찾기 위해 --> 1이 아닌 아무 노드에서 시작해도 상관없다. --> 어느 노드를 루트로 하든 가장 깊고 거리가 먼 노드를 찾는 작업.
    
    chk = [0] * (n+1)
    chk[start_node] = 1
    dfs(start_node,0) # 가장 깊고 먼 노드에서 다시 가장 깊고 먼 노드를 찾았을 때가 임의의 두 점 사이의 거리중 가장 긴 것.
    print(result)
