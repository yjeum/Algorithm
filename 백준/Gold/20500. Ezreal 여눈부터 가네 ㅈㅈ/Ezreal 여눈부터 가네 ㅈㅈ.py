def solve(N):
    dp = [[0] * 15 for _ in range(N+1)]
    dp[0][0] = 1
    
    for digit in range(1, N+1):
        for mod15 in range(15):
            # 1을 추가하는 경우
            new_mod15 = (mod15 * 10 + 1) % 15
            dp[digit][new_mod15] = (dp[digit][new_mod15] + dp[digit-1][mod15]) % 1000000007
                
            # 5를 추가하는 경우
            new_mod15 = (mod15 * 10 + 5) % 15
            dp[digit][new_mod15] = (dp[digit][new_mod15] + dp[digit-1][mod15]) % 1000000007
    
    return dp[N][0]

N = int(input())
print(solve(N))
