import sys
from collections import deque

input = sys.stdin.readline

didj = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def melt(arr):
    n_arr = [[0] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):

            if arr[i][j] != 0:
                temp = 0
                for di, dj in didj:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0:
                        temp += 1

                n_arr[i][j] = arr[i][j] - temp
                if n_arr[i][j] < 0:
                    n_arr[i][j] = 0

    return n_arr


def bfs(n_arr):
    visited = [[0] * (M) for _ in range(N)]
    q = deque([])
    cnt = 0
    for i in range(N):
        for j in range(M):

            if n_arr[i][j] != 0 and visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    ci, cj = q.popleft()
                    for di, dj in didj:
                        ni, nj = ci + di, cj + dj
                        if n_arr[ni][nj] != 0 and visited[ni][nj] == 0:
                            q.append((ni, nj))
                            visited[ni][nj] = 1
                cnt += 1

    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0

while True:
    arr = melt(arr)
    cnt = bfs(arr)

    if cnt == 0:
        print(0)
        break
    elif cnt == 1:
        time += 1
    else:
        print(time + 1)
        break
