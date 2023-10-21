import sys
input = sys.stdin.readline

def dfs(i, j):
    if i == N - 1 and j == M - 1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[i][j] > arr[ni][nj]:
            dp[i][j] += dfs(ni, nj)

    return dp[i][j]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

result = dfs(0, 0)
print(result)