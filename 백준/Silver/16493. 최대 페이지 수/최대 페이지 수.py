import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 챕터에 관한 소요되는 일 수 및 페이지 수 정보
info = [[0, 0]]
for _ in range(M):
    info.append(list(map(int, input().split())))

# knapsack 정보 업데이트
knapsack = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(1, M + 1):  # 챕터 관련
    for j in range(1, N + 1):  # 소요 일수 관련

        # 소요 일수보다 기준이 작은 경우
        if j < info[i][0]:
            knapsack[i][j] = knapsack[i - 1][j]
        # 현재 챕터터에 관한 정보를 사용하는 경우
        else:
            # 사용하지 않는 경우, 사용하는 경우 비교
            knapsack[i][j] = max(
                knapsack[i - 1][j], info[i][1] + knapsack[i - 1][j - info[i][0]]
            )
print(knapsack[M][N])
