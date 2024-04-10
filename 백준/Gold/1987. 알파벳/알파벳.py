import sys

input = sys.stdin.readline


def DFS(ci, cj, visited_lst, N, M, cnt):
    
    global max_cnt

    max_cnt = max(max_cnt, cnt)

    for i in range(4):
        ni, nj = dx[i] + ci, dy[i] + cj

        if 0 <= ni < N and 0 <= nj < M:
            if visited_lst[ord(map[ni][nj]) - ord('A')] == 0:
                visited_lst[ord(map[ni][nj]) - ord('A')] = 1
                DFS(ni, nj, visited_lst, N, M, cnt + 1)
                visited_lst[ord(map[ni][nj]) - ord('A')] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

map = [input().rstrip() for _ in range(N)]

visited_lst = [0] * 26
visited_lst[ord(map[0][0]) - ord('A')] = 1

max_cnt = 0
DFS(0, 0, visited_lst, N, M, 1)

print(max_cnt)
