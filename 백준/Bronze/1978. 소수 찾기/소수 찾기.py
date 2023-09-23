import sys

N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in num_lst:
    flg = True
    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            flg = False
            break
    if flg == True:
        cnt += 1

print(cnt)