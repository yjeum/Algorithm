import sys
input = sys.stdin.readline

didj = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def check(ci, cj):
    cnt = 0
    for di, dj in didj:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "X":
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False


N, M = map(int, input().split())
arr = list(input() for _ in range(N))

land = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == "X" and check(i, j):
            land.append((i, j))

left = min(land, key=lambda x: x[1])[1]
right = max(land, key=lambda x: x[1])[1]
top = min(land, key=lambda x: x[0])[0]
bottom = max(land, key=lambda x: x[0])[0]

after_land = [["."] * (right - left + 1) for _ in range(bottom - top + 1)]
for li, lj in land:
    after_land[li - top][lj - left] = "X"

for pi in range(bottom - top + 1):
    print("".join(after_land[pi]))
