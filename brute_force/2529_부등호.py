# https://www.acmicpc.net/problem/2529
# 부등호

import sys
def sign_order(idx,nums):
    if idx < 0: # 0이하가되면 배열 밖의 인덱스
        return
    if signs[idx] == '>' and nums[idx] > nums[idx+1]: # 부등호대로 맞으면 빠지기
        return
    if signs[idx] == '<' and nums[idx] < nums[idx+1]: # 부등호대로 맞으면 빠지기
        return
    nums[idx],nums[idx+1] = nums[idx+1],nums[idx] # 부등호대로 결과가 틀리면 위치 변경
    sign_order(idx-1,nums) # 처음까지 비교하면서 확인

if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    signs = list(map(str,read().split()))
    max_num = [9,8,7,6,5,4,3,2,1,0]
    min_num = [0,1,2,3,4,5,6,7,8,9]
    
    for i in range(n): # 부등호에 맞게 배열 정렬
        sign_order(i,max_num)
        sign_order(i,min_num)
    print(''.join(map(str,max_num[:n+1])))
    print(''.join(map(str,min_num[:n+1])))
