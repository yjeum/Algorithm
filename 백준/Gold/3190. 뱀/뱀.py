import sys

input = sys.stdin.readline

from collections import deque

# 보드판
N = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]

# 사과
# 사과가 존재하면 1
apple = int(input())
for _ in range(apple):
    x, y = map(int, input().split())
    board[x][y] = 1

# 방향
change = int(input())
change_list = []
for _ in range(change):
    order, dir = input().split()
    change_list.append((int(order), dir))
current_change = 0

# 뱀의 이동
snack = deque([(1, 1)])

dir_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
current_dir = 0
cnt = 0

# 뱀의 몸이 존재하면 2
board[1][1] = 2
c_x, c_y = 1, 1

while snack:
    # 방향전환 관련
    if cnt == change_list[current_change][0]:
        if change_list[current_change][1] == "D":
            current_dir = (current_dir + 1) % 4
        else:
            current_dir = (current_dir + 3) % 4

        if current_change < len(change_list) - 1:
            current_change += 1

    # 다음 머리 위치 관련
    n_x, n_y = c_x + dir_list[current_dir][0], c_y + dir_list[current_dir][1]
    if 1 <= n_x <= N and 1 <= n_y <= N and board[n_x][n_y] != 2:
        cnt += 1
        snack.append((n_x, n_y))
        c_x, c_y = n_x, n_y
        # 사과가 없다면 꼬리 이동
        if board[n_x][n_y] == 0:
            tail_x, tail_y = snack.popleft()
            board[tail_x][tail_y] = 0
        board[n_x][n_y] = 2
    else:
        print(cnt + 1)
        break
