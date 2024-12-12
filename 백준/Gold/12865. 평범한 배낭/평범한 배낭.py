import sys
input = sys.stdin.readline

# 물품 수, 최대 무게
N, M = map(int, input().split())

# 물건 리스트(무게, 가치)
suff = [[0, 0]]
for _ in range(N):
    suff.append(list(map(int, input().split())))

# knapsack 정보 업데이트
knapsack = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):  # 물품 관련
    for j in range(1, M + 1):  # 현재 배낭 무게 관련
        w, v = suff[i][0], suff[i][1]

        # 현재 물품만 담는다고 해도 담지 못하는 경우
        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        # 현재 물품을 가지고 판단 진행
        else:
            # 현재 물품을 넣지 않는 경우, 넣는 경우 비교
            knapsack[i][j] = max(knapsack[i - 1][j], v + knapsack[i - 1][j - w])
print(knapsack[N][M])
