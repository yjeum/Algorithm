def honey(n, honey_sum, honey_tmp, i, j):
    global honey_max
    if honey_sum > C:
        return
    if n == M:
        honey_max = max(honey_max, honey_tmp)
        return
    honey(n + 1, honey_sum + honeycomb[i][j + n], honey_tmp + (honeycomb[i][j + n] ** 2), i, j)
    honey(n + 1, honey_sum, honey_tmp, i, j)


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())

    honeycomb = [list(map(int, input().split())) for _ in range(N)]

    honey_res = 0
    for i1 in range(N):
        for j1 in range(N - M + 1):
            honey_max = 0
            honey(0, 0, 0, i1, j1)
            honey1_max = honey_max
            for i2 in range(i1, N):
                if i1 == i2:
                    startj = j1 + M
                else:
                    startj = 0
                for j2 in range(startj, N - M + 1):
                    honey_max = 0
                    honey(0, 0, 0, i2, j2)
                    honey2_max = honey_max
                    honey_res = max(honey_res, honey1_max + honey2_max)

    print(f"#{tc}", honey_res)
