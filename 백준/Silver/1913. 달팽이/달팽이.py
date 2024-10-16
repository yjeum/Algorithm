import sys

input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())
arr = [[0] * N for _ in range(N)]
arr[N // 2][N // 2] = 1

cur = 1
c_di = 0
ci, cj = N // 2, N // 2
step = 1
c_step = 0
flag = False

while cur < N * N:

    ci, cj = ci + direction[c_di][0], cj + direction[c_di][1]
    cur += 1
    arr[ci][cj] = cur
    c_step += 1

    if c_step == step:
        c_step = 0
        c_di = (c_di + 1) % 4
        # step 증가여부 확인
        if flag == True:
            flag = False
            step += 1
        else:
            flag = True

check = int(input())
a_i, a_j = 0, 0
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
        if arr[i][j] == check:
            a_i, a_j = i, j
    print()
print(a_i + 1, a_j + 1)
