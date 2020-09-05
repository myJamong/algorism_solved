# https://www.acmicpc.net/problem/16964
# DFS 스페셜 저지

import sys
def dfs(node):
    global res_idx
    global flag
    if not flag:
        return
    if res[res_idx] != node: # 방문 순서 확인
        flag = False
        return
    res_idx += 1
    for i in arr[node]:
        if chk[i] == 0:
            chk[i] = 1
            dfs(i)

if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [[] for _ in range(n+1)]
    chk = [0] * (n+1)
    order = [0] * (n+1)
    for _ in range(n-1): # 연결 정보 저장
        a,b = map(int,read().split())
        arr[a].append(b)
        arr[b].append(a)
    res = [0] + list(map(int,read().split()))
    res_idx = 1
    flag = True
    for i in range(1,n+1): # 확인하는 방문 순서대로 순위를 매긴다.
        order[res[i]] = i
    for i in arr: # 각 연결 정보에 대해서 확인 순서대로 정렬하는 작업.
        i.sort(key=lambda x:order[x])
    chk[1] = 1
    dfs(1)
    print(1 if flag else 0)
