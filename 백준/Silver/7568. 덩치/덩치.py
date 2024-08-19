import sys
input = sys.stdin.readline

N = int(input())
body = [list(map(int, input().split())) for _ in range(N)]
for c_height, c_weight in body:
    rank = 1
    for n_height, n_weight in body:
        if c_height < n_height and c_weight < n_weight:
            rank += 1
    print(rank, end=" ")
