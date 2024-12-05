import sys
input = sys.stdin.readline

didj = [[-1, 0], [1, 0], [0, 1], [0, -1]]


# 상어 이동 함수
def move_sharks():
    global sharks, sea
    temp_sea = [[0] * C for _ in range(R)]
    new_sharks = {}

    for idx, shark in sharks.items():
        ci, cj, s, d, z = shark
        if d in [0, 1]:
            s %= 2 * (R - 1)
        else:
            s %= 2 * (C - 1)

        # 상어 이동
        for _ in range(s):
            ni, nj = ci + didj[d][0], cj + didj[d][1]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                d = (d + 1) % 2 if d < 2 else 2 + (d + 1) % 2
                ni, nj = ci + didj[d][0], cj + didj[d][1]
            ci, cj = ni, nj

        # 이동한 상어의 위치 업데이트
        if temp_sea[ci][cj]:
            # 이미 상어가 있으면 크기 비교
            other_idx = temp_sea[ci][cj]
            if sharks[other_idx][4] < z:
                del new_sharks[other_idx]
                temp_sea[ci][cj] = idx
                new_sharks[idx] = [ci, cj, s, d, z]
        else:
            temp_sea[ci][cj] = idx
            new_sharks[idx] = [ci, cj, s, d, z]

    sea = temp_sea
    sharks = new_sharks


R, C, M = map(int, input().split())
sharks = {}
sea = [[0] * C for _ in range(R)]
for idx in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    sea[r - 1][c - 1] = idx
    sharks[idx] = [r - 1, c - 1, s, d - 1, z]

weight = 0

# 낚시왕 이동 및 상어 낚시
for j in range(C):
    # 1. 낚시왕이 있는 열에서 가장 가까운 상어 잡기
    for i in range(R):
        if sea[i][j]:
            shark_idx = sea[i][j]
            weight += sharks[shark_idx][4]
            del sharks[shark_idx]
            sea[i][j] = 0
            break

    # 2. 상어 이동
    move_sharks()

print(weight)
