import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1e9 for _ in range(3)] for _ in range(M)] for _ in range(N)]

# 첫번째 줄 세팅
for set_j in range(M):
    for set_k in range(3):
        dp[0][set_j][set_k] = arr[0][set_j]

# dp 계산
for i in range(1, N):
    for j in range(M):
        for k in range(3):
            # 가장자리 처리
            if (j == 0 and k == 0) or (j == M - 1 and k == 2):
                continue

            # 방향 확인 후 처리
            if k == 0:
                dp[i][j][0] = arr[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            elif k == 1:
                dp[i][j][1] = arr[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            else:
                dp[i][j][2] = arr[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

min_val = 1e9
for find_j in range(M):
    min_in_j = min(dp[N - 1][find_j])
    min_val = min(min_val, min_in_j)
print(min_val)
