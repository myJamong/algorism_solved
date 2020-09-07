# https://www.acmicpc.net/problem/2250
# 트리의 높이와 너비

import sys
def in_order(node): # 중위 순회
    global idx
    if node in tree:
        if level[node] == 0:
            level[node] = level[parent[node]] + 1 # 각 노드의 레벨 저장
        in_order(tree[node][0])
        
        if idx < level_min[level[node]]:
            level_min[level[node]] = idx # 레벨의 위치상 가장 좌측에 있는 값 저장
        if idx > level_max[level[node]]:
            level_max[level[node]] = idx # 레벨의 위치상 가장 우측에 있는 값 저장
        idx += 1
        
        in_order(tree[node][1])

if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    tree = {}
    parent = [0] * (n+1)
    level_min = [n+1] * (n+1) # 각 레벨당 가장 좌측
    level_max = [0] * (n+1) # 각 레벨당 가장 우측
    level = [0] * (n+1) # 각 노드의 레벨
    idx = 1 # 위치 표기용
    
    for _ in range(n): # 트리 만들기
        node,l,r = map(int,read().split())
        if l != -1:
            parent[l] = node
        if r != -1:
            parent[r] = node
        tree[node] = (l,r)
        
    root = 1
    for i in range(1,n+1): # 루트 노드 찾기 --> 루트노드부터 입력이 주어진다는 보장 없음
        if parent[i] == 0:
            root = i
            break
    level[root] = 1 # 루트의 레벨은 1
    in_order(root) # 중위 순회
    
    result = result_lv = 0
    for i in range(1,n+1): 결과 확인
        diff = level_max[i] - level_min[i] + 1
        if result < diff: # 더 큰 값만 찾으므로 가장 낮은 레벨의 값으로 유지
            result = diff
            result_lv = i
    print(result_lv,result)
