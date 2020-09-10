# https://www.acmicpc.net/problem/1202
# 보석 도둑

import sys
import heapq
if __name__ == "__main__":
    read = sys.stdin.readline
    n,k = map(int,read().split())
    jewels = []
    for _ in range(n):
        m,v = map(int,read().split())
        heapq.heappush(jewels,(m,v)) # 리스트말고 힙큐나 우선순위큐를 사용하자 --> 리스트 사용하면 다시한번 정렬작업을 아래서 해줘야한다.
    bags = [int(read()) for _ in range(k)]
    bags.sort()
    
    result = 0
    temp = []
    for bag in bags:
        while jewels and bag >= jewels[0][0]: # 가방 안에 보석이 들어갈 수 있는 경우
            m,v = heapq.heappop(jewels) # 보석 최소힙에서 빼고
            heapq.heappush(temp,-v) # 보석 최대힙으로 이동
        if temp: --> 이거를 확인해주는게 가방은 있는데 보석이 없는 경우가 있고 더 작은 가방에 제일 큰 보석을 넣은 경우 더 큰 가방에 나머지 남은 보석들을 순차적으로 넣어줘야한다.
            result -= heapq.heappop(temp) # 가방에 넣을 수 있는 보석이 존재한다면 결과에 합친다.
        elif not jewels:
            break        
    print(result)
