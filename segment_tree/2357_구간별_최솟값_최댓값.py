# https://www.acmicpc.net/problem/2357
# 구간별 최솟값 최댓값
import math
import sys

def tree_min_init(n,s,e):
    if s == e:
        tree_min[n] = arr[s]
    else:
        tree_min_init(n*2,s,(s+e)//2)
        tree_min_init(n*2+1,(s+e)//2+1,e)
        tree_min[n] = min(tree_min[n*2],tree_min[n*2+1])
        
def tree_max_init(n,s,e):
    if s == e:
        tree_max[n] = arr[s]
    else:
        tree_max_init(n*2,s,(s+e)//2)
        tree_max_init(n*2+1,(s+e)//2+1,e)
        tree_max[n] = max(tree_max[n*2],tree_max[n*2+1])

def tree_min_query(n,s,e,l,r):
    if s > r or e < l:
        return 1000000000
    if s >= l and e <= r:
        return tree_min[n]
    return min(tree_min_query(n*2,s,(s+e)//2,l,r),tree_min_query(n*2+1,(s+e)//2+1,e,l,r))

def tree_max_query(n,s,e,l,r):
    if s > r or e < l:
        return 0
    if s >= l and e <= r:
        return tree_max[n]
    return max(tree_max_query(n*2,s,(s+e)//2,l,r),tree_max_query(n*2+1,(s+e)//2+1,e,l,r))

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    tree_min = [0] * pow(2,math.ceil(math.log(len(arr),2))+1)
    tree_max = [0] * len(tree_min)
    
    tree_min_init(1,0,len(arr)-1)
    tree_max_init(1,0,len(arr)-1)
    
    for i in range(m):
        a,b = map(int,sys.stdin.readline().split())
        min_num = tree_min_query(1,0,len(arr)-1,a-1,b-1)
        max_num = tree_max_query(1,0,len(arr)-1,a-1,b-1)
        print(min_num,max_num)  
