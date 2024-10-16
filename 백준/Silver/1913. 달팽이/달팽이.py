import sys

input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())
target = int(input())
arr = [[0] * N for _ in range(N)]
arr[N // 2][N // 2] = 1

cur = 1
c_di = 0
ci, cj = N // 2, N // 2
step = 1
c_step = 0
flag = False
answer = [1, 1]

while cur < N * N:

    if arr[ci][cj] == target:
        answer = [ci + 1, cj + 1]

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

for i in range(N):
    print(" ".join(map(str, arr[i])))
print(" ".join(map(str, answer)))