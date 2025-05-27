import sys

input = sys.stdin.readline

dice_pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
for i in range(6):
    cnt = 0
    tnv = dices[0][i]
    temp_max = 0
    while cnt < N:

        bni = dices[cnt].index(tnv)
        tnv = dices[cnt][dice_pair[bni]]

        if dices[cnt][bni] != 6 and tnv != 6:
            temp_max += 6
        elif dices[cnt][bni] != 5 and tnv != 5:
            temp_max += 5
        else:
            temp_max += 4

        cnt += 1

    max_val = max(max_val, temp_max)
print(max_val)
