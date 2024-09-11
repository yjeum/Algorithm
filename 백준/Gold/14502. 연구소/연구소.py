import sys
from collections import deque
import copy

input = sys.stdin.readline

didj = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs():
    global max_wall, safe_zone
    temp_cnt = safe_zone - 3

    q = deque(vi)
    temp_arr = copy.deepcopy(arr)
    while q:
        ci, cj = q.popleft()

        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and temp_arr[ni][nj] == 0:
                temp_arr[ni][nj] = 2
                temp_cnt -= 1
                q.append((ni, nj))

    max_wall = max(max_wall, temp_cnt)
    return


def back_tracking(cur_wall):
    if cur_wall == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                # 벽 세우기
                arr[i][j] = 1
                # 추가 벽 세우기
                back_tracking(cur_wall + 1)
                # 원상복귀
                arr[i][j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_wall = 0
cur_wall = 0
safe_zone = 0

vi = []
# 바이러스 위치 확인
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            vi.append((i, j))
        elif arr[i][j] == 0:
            safe_zone += 1

back_tracking(0)
print(max_wall)
