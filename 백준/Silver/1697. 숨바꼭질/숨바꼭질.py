import sys
from collections import deque

input = sys.stdin.readline

def BFS(N, K):
    q = deque([(N, 0)])
    # visited를 통해 메모리 관리
    # +1, -1은 서로 번갈아 진행되기 때문에 방문 관리가 필요
    visited = [0] * 100001
    visited[N] = 1

    while q:
        now, cnt = q.popleft()

        if now == K:
            return cnt
        
        movement = [now + 1, now - 1, now * 2]
        for next_m in movement:
            # 확인 순서 중요
            # visited 먼저 확인 할 경우 index_error 발생
            if 0 <= next_m <= 100000 and visited[next_m] == 0:
                q.append((next_m, cnt + 1))
                visited[next_m] = 1

N, K = map(int, input().split())

print(BFS(N, K))