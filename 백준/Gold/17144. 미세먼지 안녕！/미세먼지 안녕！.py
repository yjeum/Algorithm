import sys

input = sys.stdin.readline

didj = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def diffusion(room):

    after_room = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 공기청정기
            if room[i][j] == -1:
                after_room[i][j] = -1

            # 미세먼지
            elif room[i][j] != 0:
                diffusion_air = room[i][j] // 5
                diffusion_cnt = 0

                for di, dj in didj:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        after_room[ni][nj] += diffusion_air
                        diffusion_cnt += 1

                after_room[i][j] += room[i][j] - (diffusion_air * diffusion_cnt)

    return after_room


def refresh(room):
    # 시계 반대방향 회전
    lo, temp = 0, 0
    ci, cj = air_purifiers[0], 0

    while True:
        ni, nj = ci + didj[lo][0], cj + didj[lo][1]

        # 공기청정기로 돌아온 경우
        if ni == air_purifiers[0] and nj == 0:
            break

        # 방향회전 필요한 경우
        if ni == R or nj == C or ni == -1 or nj == -1:
            lo = (lo + 1) % 4
            continue

        # 값 변경
        room[ni][nj], temp = temp, room[ni][nj]
        ci, cj = ni, nj

    # 시계 방향 회전
    lo, temp = 0, 0
    ci, cj = air_purifiers[1], 0

    while True:
        ni, nj = ci + didj[lo][0], cj + didj[lo][1]

        # 공기청정기로 돌아온 경우
        if ni == air_purifiers[1] and nj == 0:
            break

        # 방향회전 필요한 경우
        if ni == R or nj == C or ni == -1 or nj == -1:
            lo = (lo - 1) % 4
            continue

        # 값 변경
        room[ni][nj], temp = temp, room[ni][nj]
        ci, cj = ni, nj

    return room


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

air_purifiers = [i for i in range(R) if room[i][0] == -1]

for _ in range(T):
    room = refresh(diffusion(room))

dust = 2
for i in range(R):
    dust += sum(room[i])
print(dust)
