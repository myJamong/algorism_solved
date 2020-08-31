# https://www.acmicpc.net/problem/15954
# 인형들
# Python3로 제출하면 시간 초과가 계속해서 발생 --> PyPy3로 제출
# 둘은 동일한 문법을 지원하지만 PyPy3가 메모리를 더 많이 사용한다. 대신 빠른
# 내부적으로 다르게 동작

import sys
def std(arr): # 표준편차 구하는 함수
    m = sum(arr)/len(arr)
    temp = 0
    for i in arr:
        temp += (i-m)**2
    return (temp/len(arr))**0.5
    
if __name__ == "__main__":
    read = sys.stdin.readline
    n,k = map(int,read().split())
    arr = list(map(int,read().split()))
    result = sys.maxsize
    for i in range(0,n-k+1):
        for j in range(i+k,n+1):
            temp = std(arr[i:j])
            if result > temp:
                result = temp
    print('%.6f' % result)
