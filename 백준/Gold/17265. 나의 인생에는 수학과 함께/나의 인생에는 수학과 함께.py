import sys

input = sys.stdin.readline

didj = [[1, 0], [0, 1]]


def dfs(i, j, curr_num, before):
    global max_v, min_v

    if i == N - 1 and j == N - 1:
        max_v = max(max_v, int(curr_num))
        min_v = min(min_v, int(curr_num))

    for k in range(2):
        ni = i + didj[k][0]
        nj = j + didj[k][1]

        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj].isdigit():
                if before == "+":
                    dfs(ni, nj, int(curr_num) + int(arr[ni][nj]), "")
                elif before == "-":
                    dfs(ni, nj, int(curr_num) - int(arr[ni][nj]), "")
                elif before == "*":
                    dfs(ni, nj, int(curr_num) * int(arr[ni][nj]), "")

            else:
                dfs(ni, nj, curr_num, arr[ni][nj])


N = int(input())
arr = list(input().split() for _ in range(N))

max_v = -1e9
min_v = 1e9

dfs(0, 0, arr[0][0], "")
print(max_v, min_v)
