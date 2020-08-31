# https://www.acmicpc.net/problem/11054
# 가장 긴 바이토닉 부분 수열

import sys
if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    arr = [0] + list(map(int,read().split()))
    dpf = [0] * (n+1) # 앞에서 부터 증가하는 가장 긴 부분 수열
    dpb = [0] * (n+1) # 뒤에서 부터 증가하는 가장 긴 부분 수열
    dpf[1] = dpb[n] = 1
    for i in range(2,n+1): # 앞에서부터 확인
        temp = []
        for j in range(1,i):
            if arr[j] < arr[i]:
                temp.append(dpf[j])
        dpf[i] = max(temp)+1 if temp else 1
    for i in range(n-1,0,-1): # 뒤에서부터 확인
        temp = []
        for j in range(n,i,-1):
            if arr[j] < arr[i]:
                temp.append(dpb[j])
        dpb[i] = max(temp)+1 if temp else 1
    result = 0   
    for i in range (1,n+1): # 결과 확인
        length = dpf[i] + dpb[i] - 1
        if result < length:
            result = length
    print(result)
