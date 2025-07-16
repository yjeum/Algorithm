import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
temp_left = [[0] * M for _ in range(N)]
temp_right = [[0] * M for _ in range(N)]

# 첫 줄은 오른쪽 방향으로 더하는 것만 가능
dp[0][0] = arr[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i - 1] + arr[0][i]

# 왼쪽, 오른쪽, 아래쪽만 탐색 가능
for i in range(1, N):
    # 첫번쨰 칸은 내려온 값 그대로
    temp_left[i][0] = dp[i - 1][0] + arr[i][0]
    temp_right[i][M - 1] = dp[i - 1][M - 1] + arr[i][M - 1]

    for j in range(1, M):

        # 왼쪽에서 오는 경우
        temp_left[i][j] = max(temp_left[i][j - 1], dp[i - 1][j]) + arr[i][j]
        # 오른쪽에서 오는 경우
        temp_right[i][M - 1 - j] = (
            max(temp_right[i][M - 1 - j + 1], dp[i - 1][M - 1 - j]) + arr[i][M - 1 - j]
        )

    for j in range(M):
        dp[i][j] = max(temp_left[i][j], temp_right[i][j])

print(dp[N - 1][M - 1])
