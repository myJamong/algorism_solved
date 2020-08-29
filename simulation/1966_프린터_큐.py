# https://www.acmicpc.net/problem/1966
# 프린터 큐. 지시에 따라 그대로 수행

import sys
if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        doc_cnt,find_doc_idx = map(int,sys.stdin.readline().split())
        temp = list(map(int,sys.stdin.readline().split()))
        q = []
        for i in range(len(temp)): # 인덱스 정보와 함께 큐에 저장
            q.append((i,temp[i]))
        cnt = 0
        while True:
            max_val = max(q,key=lambda x:x[1]) # 현재 큐의 최대 값
            if max_val[1] == q[0][1]: # 최대 값이 큐의 가장 처음에 있는 경우
                cnt += 1
                if find_doc_idx == q[0][0]: # 찾으려는 값의 프린트하는 경우
                    break
                q.pop(0) # 프린터에서 출력
            else:
                q.append(q.pop(0)) # 우선순위가 아니므로 큐의 맨 뒤로 보낸다.
        print(cnt)
