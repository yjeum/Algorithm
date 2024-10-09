import sys
from collections import deque

input = sys.stdin.readline

didj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]


def bfs():
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1
    q = deque([(0, 0, 0, K)])

    while q:

        ccnt, ci, cj, ck = q.popleft()

        if ci == N - 1 and cj == M - 1:
            return ccnt

        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if (
                0 <= ni < N
                and 0 <= nj < M
                and arr[ni][nj] == 0
                and visited[ni][nj][ck] == 0
            ):
                q.append((ccnt + 1, ni, nj, ck))
                visited[ni][nj][ck] = 1

        if ck > 0:
            for di, dj in horse:
                ni, nj = ci + di, cj + dj
                if (
                    0 <= ni < N
                    and 0 <= nj < M
                    and arr[ni][nj] == 0
                    and visited[ni][nj][ck-1] == 0
                ):
                    q.append((ccnt + 1, ni, nj, ck - 1))
                    visited[ni][nj][ck-1] = 1

    return -1


K = int(input())
M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
