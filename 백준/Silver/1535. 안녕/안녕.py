import sys
input = sys.stdin.readline

# 총인원
N = int(input())
# 사용되는 체력, 얻는 기쁨 관련 리스트
hp = [0] + list(map(int, input().split()))
joy = [0] + list(map(int, input().split()))

# knapsack 정보 업데이트
knapsack = [[0] * (100) for _ in range(N + 1)]
for i in range(1, N + 1):  # 만나는 사람
    for j in range(1, 100):  # 사용된 체력

        # 현재 만나는 사람만 인사했을 때에도 체력이 부족한 경우
        if j < hp[i]:
            knapsack[i][j] = knapsack[i - 1][j]
        # 현재 만나는 사람과 인사가 가능한 경우
        else:
            # 인사를 하는 경우, 하지 않는 경우 비교
            knapsack[i][j] = max(
                knapsack[i - 1][j], joy[i] + knapsack[i - 1][j - hp[i]]
            )

print(knapsack[N][99])
