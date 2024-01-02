import sys
from collections import deque

input = sys.stdin.readline


def find_I():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                return i, j


def find_friend(campus):
    visited = [[0] * M for _ in range(N)]

    start_i, start_j = find_I()

    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = 1
    cnt = 0

    while q:
        i, j = q.popleft()

        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < N
                and 0 <= nj < M
                and campus[ni][nj] != "X"
                and visited[ni][nj] == 0
            ):
                q.append((ni, nj))
                visited[ni][nj] = 1
                if campus[ni][nj] == "P":
                    cnt += 1
    if cnt != 0:
        return cnt
    else:
        return "TT"


N, M = map(int, input().split())

campus = [list(input().rstrip()) for _ in range(N)]

print(find_friend(campus))
