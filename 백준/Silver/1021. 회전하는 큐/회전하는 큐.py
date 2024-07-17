from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
target_list = list(map(int, input().split()))
q = deque([i for i in range(1, N+1)])
cnt = 0

for target in target_list:

    while True:
        # 타겟을 꺼낼 수 있는지 확인
        if q[0] == target:
            q.popleft()
            break

        else:
            # 현재 위치에서 왼쪽으로 돌릴지, 오른쪽으로 돌릴지 결정
            if q.index(target) < len(q)/2:
                while q[0] != target:
                    q.append(q.popleft())  
                    cnt += 1
            else:   
                while q[0] != target:
                    q.appendleft(q.pop())  
                    cnt += 1
print(cnt)