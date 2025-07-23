import sys
from collections import deque

input = sys.stdin.readline

didj = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def bfs(mi, mj):
    global cnt
    # 아직 봉우리 여부 판단 전
    flg = True

    # 같은 높이를 돌면서 인접한 지역에 더 높은 높이가 있는지 여부 판단
    q = deque([(mi, mj)])
    while q:
        ci, cj = q.popleft()
        # 방문처리
        visited[ci][cj] = 1

        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                # 같은 높이이면서 방문한 기록이 없는지 확인
                if arr[ni][nj] == arr[ci][cj] and visited[ni][nj] == 0:
                    q.append((ni, nj))
                # 인접한 곳에 높은 곳이 있는지 판단
                elif arr[ni][nj] > arr[ci][cj]:
                    flg = False

    if flg == True:
        cnt += 1

    return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            bfs(i, j)

print(cnt)
