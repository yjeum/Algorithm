import sys

input = sys.stdin.readline


def check(switch):
    temp_max_candy = 1
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if switch[i][j] == switch[i][j - 1]:
                temp += 1
            else:
                temp_max_candy = max(temp_max_candy, temp)
                temp = 1
            temp_max_candy = max(temp_max_candy, temp)

        temp = 1
        for j in range(1, N):
            if switch[j][i] == switch[j - 1][i]:
                temp += 1
            else:
                temp_max_candy = max(temp_max_candy, temp)
                temp = 1
            temp_max_candy = max(temp_max_candy, temp)

    return temp_max_candy


N = int(input())
board = [list(input()) for _ in range(N)]

max_candy = 0
for i in range(N):
    for j in range(N - 1):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            max_candy = max(max_candy, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            max_candy = max(max_candy, check(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(max_candy)
