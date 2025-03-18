import sys
input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = [list(map(int, input().split())) for _ in range(N)] + [[D + 10, 0, 0]]
shortcuts.sort(key=lambda x: x)

dp = [0] + [i for i in range(D + 1)]
s_idx = 0

for cur in range(1, D + 2):
    # 이전 값과 비교하여 현재 값 갱신
    dp[cur] = min(dp[cur - 1] + 1, dp[cur])

    # 지름길을 활용한 값 갱신
    while shortcuts[s_idx][0] == cur - 1:
        if shortcuts[s_idx][1] <= D:
            dp[shortcuts[s_idx][1] + 1] = min(
                dp[shortcuts[s_idx][1] + 1], dp[cur] + shortcuts[s_idx][2]
            )
        s_idx += 1


print(dp[D + 1])
