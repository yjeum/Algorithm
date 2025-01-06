import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    q = deque([(start_x, start_y)])
    visited = [0] * N
    while q:
        x, y = q.popleft()
        # 페스티벌 도착 가능
        if abs(x - target_x) + abs(y - target_y) <= 1000:
            print("happy")
            return
        # 아직 페스티벌까지는 도달하지 못할 때
        # 편의점 도착 가능 여부 확인
        for i in range(N):
            if visited[i] == 0:
                store_x, store_y = store[i][0], store[i][1]
                if abs(x - store_x) + abs(y - store_y) <= 1000:
                    visited[i] = 1
                    q.append((store_x, store_y))
    print("sad")
    return


T = int(input())
for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    store = []
    for _ in range(N):
        x, y = map(int, input().split())
        store.append((x, y))
    target_x, target_y = map(int, input().split())
    BFS()
