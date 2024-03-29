N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

min_cnt = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for l in range(8):
                if (i+k + j+l) % 2 == 0:
                    if board[i+k][j+l] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if board[i+k][j+l] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1

        min_cnt = min(min_cnt, cnt1, cnt2)
print(min_cnt)