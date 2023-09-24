N = int(input())

i = 0
cnt = 0
min_cnt = 5000

while i <= N // 5:
    if (N-5*i) % 3 == 0:
        j = (N - 5*i) // 3
        cnt = i + j

        if min_cnt >= cnt:
            min_cnt = cnt
    i += 1

if min_cnt == 5000:
    print(-1)
else:
    print(min_cnt)