import sys

input = sys.stdin.readline

didj = [(0, -1), (1, 0), (0, 1), (-1, 0)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

std_dire = 0
std_step = 1
c_step = 0
ci, cj = N // 2, N // 2
flag = False

# 0 : left, 1 : down, 2 : right, 3 : up
dire = [
    [
        (-2, 0, 0.02),
        (-1, -1, 0.10),
        (-1, 0, 0.07),
        (-1, 1, 0.01),
        (0, -2, 0.05),
        (1, -1, 0.10),
        (1, 0, 0.07),
        (1, 1, 0.01),
        (2, 0, 0.02),
    ],
    [
        (-1, -1, 0.01),
        (-1, 1, 0.01),
        (0, -2, 0.02),
        (0, -1, 0.07),
        (0, 1, 0.07),
        (0, 2, 0.02),
        (1, -1, 0.10),
        (1, 1, 0.10),
        (2, 0, 0.05),
    ],
    [
        (-2, 0, 0.02),
        (-1, -1, 0.01),
        (-1, 0, 0.07),
        (-1, 1, 0.10),
        (0, 2, 0.05),
        (1, -1, 0.01),
        (1, 0, 0.07),
        (1, 1, 0.10),
        (2, 0, 0.02),
    ],
    [
        (-2, 0, 0.05),
        (-1, -1, 0.10),
        (-1, 1, 0.10),
        (0, -2, 0.02),
        (0, -1, 0.07),
        (0, 1, 0.07),
        (0, 2, 0.02),
        (1, -1, 0.01),
        (1, 1, 0.01),
    ],
]

outside = 0

while ci > 0 or cj > 0:

    c_step += 1

    ci, cj = ci + didj[std_dire][0], cj + didj[std_dire][1]
    ni, nj = ci + didj[std_dire][0], cj + didj[std_dire][1]
    sand = arr[ci][cj]

    temp = 0
    # 비율별로 모래 이동
    for di, dj, per in dire[std_dire]:
        if 0 <= ci + di < N and 0 <= cj + dj < N:
            arr[ci + di][cj + dj] += int(sand * per)
        else:
            outside += int(sand * per)
        temp += int(sand * per)

    if 0 <= ni < N and 0 <= nj < N:
        arr[ni][nj] += sand - temp
    else:
        outside += sand - temp

    arr[ci][cj] = 0

    if std_step == c_step:
        c_step = 0
        std_dire = (std_dire + 1) % 4
        if flag == True:
            flag = False
            std_step += 1
        else:
            flag = True


print(outside)
