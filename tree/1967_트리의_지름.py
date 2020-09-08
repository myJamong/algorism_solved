# https://www.acmicpc.net/problem/1967
# 트리의 지름

import sys
sys.setrecursionlimit(10**5)
def dfs(node,total):
    global result
    global start_node
    if result < total:
        result = total
        start_node = node
    if tree: # 노드가 1개밖에 없는 것을 대비하여
        for child,dist in tree[node]:
            if chk[child] == 0:
                chk[child] = 1
                dfs(child,dist+total)
    
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    chk = [0] * (n+1)
    tree = {}
    result = 0
    start_node = 1
    for _ in range(n-1): # 트리를 만들어주는데 루트의 시작을 1이 아닌 수에서 시작하는 것을 고려하여 양방향으로 만들어줌
        node,child,dist = map(int,read().split())
        if node in tree:
            tree[node].append((child,dist))
        else:
            tree[node] = [(child,dist)]
        if child in tree:
            tree[child].append((node,dist))
        else:
            tree[child] = [(node,dist)]
    chk[1] = 1
    dfs(1,0) # 1에서부터 시작하여 가장 깊고 먼 노드를 구한다.
    
    chk = [0] * (n+1)
    chk[start_node] = 1
    dfs(start_node,0) # 가장 깊고 먼 노드에서 가장 깊고 먼 노드까지의 거리가 답.
    print(result)
