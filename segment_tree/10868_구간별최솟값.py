# https://www.acmicpc.net/problem/10868
# 최소값 구간별 구하기
import math
import sys
def tree_init(n,s,e):
    if s == e:
        tree[n] = arr[s]
    else:
        tree_init(n*2,s,(s+e)//2)
        tree_init(n*2+1,(s+e)//2+1,e)
        tree[n] = min(tree[n*2],tree[n*2+1])

def tree_query(n,s,e,l,r):
    if s > r or e < l:
            return 1000000000
    if s >= l and e <= r:
        return tree[n]
    return min(tree_query(n*2,s,(s+e)//2,l,r),tree_query(n*2+1,(s+e)//2+1,e,l,r))

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    tree = [0] * int(pow(2,math.ceil(math.log(len(arr),2))+1))
    tree_init(1,0,len(arr)-1)
    for i in range(m):
        a,b = map(int,sys.stdin.readline().split())
        min_num = tree_query(1,0,len(arr)-1,a-1,b-1)
        print(min_num)
