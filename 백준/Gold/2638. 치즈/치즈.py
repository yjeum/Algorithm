import sys
from collections import deque

input = sys.stdin.readline

didj = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def bfs():
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:

                # 공기일 때는 방문 여부 확인 필요 O
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = -1

                # 치즈일 때는 방문 여부 확인 필요 X
                elif arr[ni][nj] == 1:
                    visited[ni][nj] += 1

    return visited


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0

while True:
    air = 0

    visited = bfs()
    time += 1

    # 치즈 녹이기
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                arr[i][j] = 0
            if arr[i][j] == 0:
                air += 1

    if air == N * M:
        print(time)
        break
