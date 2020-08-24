# https://www.acmicpc.net/problem/2042
# 구간 합 구하기
# 세그멘트 트리 기초틀 확인

import math
import sys # input() 사용시 시간 초과

# 트리 초기화
def tree_init(arr,tree,n,s,e):
    if s == e:
        tree[n] = arr[s]
    else:
        tree_init(arr,tree,n*2,s,(s+e)//2)
        tree_init(arr,tree,n*2+1,(s+e)//2+1,e)
        tree[n] = tree[n*2] + tree[n*2+1]

# 트리 합 구하기
def tree_sum(tree,n,s,e,l,r):
    if e < l or s > r:
        return 0
    if s >= l and e <= r:
        return tree[n]
    return tree_sum(tree,n*2,s,(s+e)//2,l,r) + tree_sum(tree,n*2+1,(s+e)//2+1,e,l,r)

# 배열 값 변경
def tree_update(arr,tree,n,s,e,idx,num,diff):
    if idx < s or idx > e:
        return
    diff = num - arr[idx]
    tree[n] += diff
    if s != e:
        tree_update(arr,tree,n*2,s,(s+e)//2,idx,num,diff)
        tree_update(arr,tree,n*2+1,(s+e)//2+1,e,idx,num,diff)
    else:
        arr[idx] = num

if __name__ == "__main__":
    n,m,k = map(int,sys.stdin.readline().split())
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    tree = [0] * pow(2,(math.ceil(math.log(len(arr),2)) + 1))
    tree_init(arr,tree,1,0,len(arr)-1)
        
    for _ in range(m+k):
        a,b,c = map(int,sys.stdin.readline().split())
        if a == 1:
            tree_update(arr,tree,1,0,len(arr)-1,b-1,c,0)
        else:
            print(tree_sum(tree,1,0,len(arr)-1,b-1,c-1))
