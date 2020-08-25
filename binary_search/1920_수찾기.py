# https://www.acmicpc.net/problem/1920
# 
import sys
def binary(find,arr,l,r):
    if l > r:
        return 0
    mid = (l+r)//2
    if find == arr[mid]:
        return 1
    elif find < arr[mid]:
        return binary(find,arr,l,mid-1)
    else:
        return binary(find,arr,mid+1,r)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    nums.sort()
    m = int(sys.stdin.readline())
    finds = list(map(int,sys.stdin.readline().split()))
    
    for i in finds:
        l,r = 0,len(nums)-1
        print(binary(i,nums,l,r))
