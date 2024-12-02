import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N == 1:
    answer = [1] * K
    print(*answer)
elif N == 2 and K == 1:
    print('1 2')
else:
    print(-1)
