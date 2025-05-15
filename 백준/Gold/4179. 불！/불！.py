import sys
from collections import deque

input = sys.stdin.readline

didj = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

# 현재 J와 불의 위치 파악
c_J = deque([])
c_F = deque([])
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "J":
            c_J.append((i, j))
            visited[i][j] = 1
        elif arr[i][j] == "F":
            c_F.append((i, j))

n_J = deque([])
n_F = deque([])
cnt = 0

while c_J:
    cnt += 1

    # 불의 이동 먼저
    while c_F:
        fi, fj = c_F.popleft()

        for di, dj in didj:
            nfi, nfj = fi + di, fj + dj
            if (
                0 <= nfi < N
                and 0 <= nfj < M
                and arr[nfi][nfj] != "#"
                and arr[nfi][nfj] != "F"
            ):
                arr[nfi][nfj] = "F"
                n_F.append((nfi, nfj))

    # J 이동
    while c_J:
        ji, jj = c_J.popleft()

        for di, dj in didj:
            nji, njj = ji + di, jj + dj

            if 0 <= nji < N and 0 <= njj < M:
                if arr[nji][njj] == "." and visited[nji][njj] == 0:
                    arr[nji][njj] == "J"
                    visited[nji][njj] = 1
                    n_J.append((nji, njj))

            else:
                print(cnt)
                sys.exit()
    c_F, c_J = n_F, n_J
    n_F, n_J = deque([]), deque([])

print("IMPOSSIBLE")
