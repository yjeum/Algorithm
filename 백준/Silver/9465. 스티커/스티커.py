import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    # 초기값 세팅
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
    if n > 1:
        dp[0][1] = stickers[0][1] + dp[1][0]
        dp[1][1] = stickers[1][1] + dp[0][0]
        
    # for문 순회하며 최대값 찾기
    for i in range(2, n):
        dp[0][i] = stickers[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = stickers[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))
