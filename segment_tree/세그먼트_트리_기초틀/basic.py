'''
세그멘트 트리를 사용하는 이유?
--> 구간 합을 구할 때 더 빠르게 연산할 수 있기 때문이다.
구간의 합을 구하는 프로그램을 짤때 for문을 이용하면 시간 복잡도가 O(N)이 된다.
세그멘트 트리를 사용하면 O(logN) 이 된다.
'''

import math
arr = [i for i in range(3,15,2)] # [3,5,7,9,11,13] 배열 생성

# Segment Tree용 배열 생성
# 배열의 크기에 따라 남는 공간이 있을 수 있고 이는 Tree의 층을 맞추기 위해 남겨진다.
# 배열의 크기가 6인 경우 4층의 Tree가 만들어진다. 2^(log6 올림 + 1) - 1
# 인덱스를 1부터 시작시키기 위해 -1은 안함
tree = [0] * (pow(2,math.ceil(math.log(len(arr),2))+1)) 

'''
Segment Tree 데이터 입력
arr : 배열
tree : 트리
n : node의 시작 --> 1 부터
s : tree에서 합산된 node값이 arr에서 다루는 범위의 시작 idx --> 0 부터
e : tree에서 합산된 node값이 arr에서 다루는 범위의 끝 idx --> arr 배열의 크기 - 1
'''
def tree_init(arr,tree,n,s,e):
    if s == e: # 리프노드에 도달한 경우
        tree[n] = arr[s]
    else:
        tree_init(arr,tree,n*2,s,(s+e)//2) # 왼쪽 자식 노드로 이동
        tree_init(arr,tree,n*2+1,(s+e)//2+1,e) # 오른쪽 자식노드로 이동
        tree[n] = tree[n*2] + tree[n*2+1] # 두 자식노드의 합산된 값을 노드에 입력
        
        
'''
배열에서 범위의 총합 구하기
tree : 트리
n : node의 시작 --> 1 부터
s : tree에서 합산된 node값이 arr에서 다루는 범위의 시작 idx --> 0 부터
e : tree에서 합산된 node값이 arr에서 다루는 범위의 끝 idx --> arr 배열의 크기 - 1
l : 합을 구해야하는 범위의 인덱스 시작
r : 합을 구해야하는 범위의 인데스 끝

'''
def tree_sum(tree,n,s,e,l,r):
    # 노드가 다루는 범위가 합을 구해야하는 범위 밖에 있는 경우
    # EX) 3 ~ 4 사이의 합을 구하는데 들린 노드가 0~1 사이를 다루는 노드인 경우
    if e < l or r < s: 
        return 0
    # 노드가 다루는 범위가 합을 구해야하는 범위 안에 있는 경우
    # EX) 3 ~ 6 사이의 합을 구하는데 들린 노드가 3 ~4 사이를 다루는 노드인 경우
    if l <= s and e <= r:
        return tree[n]
    # 그외의 나머지 경우
    # 두 범위의 일부만 겹치는 경우 범위를 좁혀나가 확인
    return tree_sum(tree,n*2,s,(s+e)//2,l,r) + tree_sum(tree, n*2+1,(s+e)//2+1,e,l,r)
   
    
'''
배열에서 값을 변경할때 Tree의 변경
a : 배열
tree : 트리
n : node의 시작 --> 1 부터
s : tree에서 합산된 node값이 arr에서 다루는 범위의 시작 idx --> 0 부터
e : tree에서 합산된 node값이 arr에서 다루는 범위의 끝 idx --> arr 배열의 크기 - 1
idx : 바꾸고자하는 인덱스
num : 변경되는 값
diff : 변경되는 값과 노드값의 차이 --> 재귀함수 호출 시 변경되어야하는 값을 넘겨주기 위해 사용. 처음에는 아무값이나 보내도 상관없음
'''
def tree_update(arr,tree,n,s,e,idx,num,diff):
    if idx < s or idx > e: # 인덱스가 범위 밖인 경우
        return
    diff =  num - arr[idx] # 변경하는 값과의 차이
    tree[n] += diff # 루트 노드부터 시작할것이기 때문에 먼저 차이를 더해준다.
    if s != e: # 리프노드가 아닌 경우
        tree_update(arr,tree,n*2,s,(s+e)//2,idx,num,diff) # 왼쪽 노드 탐색하며 수정
        tree_update(arr,tree,n*2+1,(s+e)//2+1,e,idx,num,diff) # 오른쪽 노드 탐색하며 수정
    else:
        arr[idx] = num # 리프노드에 도착했을 때 배열 정보 수정

        
tree_init(arr,tree,1,0,len(arr)-1) # 트리 초기화
print(arr,tree)
print(tree_sum(tree,1,0,len(arr)-1,4,7),'\n') # 구간 합 확인


tree_update(arr,tree,1,0,len(arr)-1,0,11,0) # 0 번째 값을 11로 변경
print(arr,tree)

tree_update(arr,tree,1,0,len(arr)-1,5,11,0) # 5 번째 값을 11로 변경
print(arr,tree)
