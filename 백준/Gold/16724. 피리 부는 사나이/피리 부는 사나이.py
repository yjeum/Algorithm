import sys

input = sys.stdin.readline


def find_safe_zone(ci, cj):
    global cnt
    stack = []

    while True:
        # 아직 방문하지 않은 곳
        if visited[ci][cj] == 0:
            visited[ci][cj] = 1
            stack.append((ci, cj))

            if arr[ci][cj] == "U":
                ci -= 1
            elif arr[ci][cj] == "D":
                ci += 1
            elif arr[ci][cj] == "L":
                cj -= 1
            else:
                cj += 1

        # 지금 진행하고 있는 사이클
        elif visited[ci][cj] == 1:
            visited[ci][cj] = 2
            cnt += 1
            for ti, tj in stack:
                visited[ti][tj] = 2
            break

        # 세이프존으로 이동가능한 길
        else:
            visited[ci][cj] = 2
            for ti, tj in stack:
                visited[ti][tj] = 2
            break

    return


N, M = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        # 아직 방문하지 않았다면 방향에 맞춰 이동
        if visited[i][j] == 0:
            find_safe_zone(i, j)

print(cnt)
