import sys
from collections import deque

input = sys.stdin.readline

def BFS(s_x, s_y):
    global max_cnt
    q = deque([(s_x, s_y)])

    visited = [[0] * col for _ in range(row)]
    visited[s_x][s_y] = 1
    while q:
        c_x, c_y = q.popleft()

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = c_x + di, c_y + dj
            if 0 <= ni < row and 0 <= nj < col and treasure_map[ni][nj] == "L" and visited[ni][nj] == 0:
                visited[ni][nj] = visited[c_x][c_y] + 1
                q.append((ni, nj))
                max_cnt = max(max_cnt, visited[ni][nj])

row, col = map(int, input().split())
treasure_map = [input().rstrip() for _ in range(row)]
max_cnt = 0

for s_x in range(row):
    for s_y in range(col):
        if treasure_map[s_x][s_y] == "L":
            BFS(s_x, s_y)
print(max_cnt - 1)