N = int(input())

score_list = list(map(int, input().split()))
dp = [0] * N

for i in range(0,N):
    for k in range(i,-1,-1):
        temp_list = score_list[k:i+1]
        tmp = max(temp_list)-min(temp_list)
        if k == 0:
            k = 1
        
        dp[i] = max(dp[i], dp[k-1] + tmp)
print(dp[-1])