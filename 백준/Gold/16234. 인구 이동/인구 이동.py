import sys
from collections import deque

input = sys.stdin.readline

didj = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

day = 0
flg = True
while flg:
    visited = [[0] * N for _ in range(N)]
    flg = False

    for i in range(N):
        for j in range(N):
            # 방문하지 않았으면 BFS로 동맹 여부 확인
            if visited[i][j] == 0:
                temp_c, temp_p = [(i, j)], arr[i][j]
                q = deque([(i, j)])
                visited[i][j] = 1

                while q:
                    ci, cj = q.popleft()
                    for di, dj in didj:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                            if L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                                flg = True
                                q.append((ni, nj))
                                temp_c.append((ni, nj))
                                temp_p += arr[ni][nj]
                                visited[ni][nj] = 1

                for qi, qj in temp_c:
                    arr[qi][qj] = temp_p // len(temp_c)

    if flg:
        day += 1

print(day)
