import sys
input = sys.stdin.readline

N, K = map(int, input().split()) 

coin_lst = []
for i in range(N):
    coin_lst.append(int(input()))

cnt = 0
for i in range(N - 1, -1, -1):
    cnt += K // coin_lst[i]
    K = K % coin_lst[i]

print(cnt)