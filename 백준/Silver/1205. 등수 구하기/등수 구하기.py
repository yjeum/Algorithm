import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())
rank = N + 1
lo = N + 1

if N > 0:
    scores = list(map(int, input().split()))

    for i in range(N):
        if rank == N + 1 and score >= scores[i]:
            rank = i + 1

        if score > scores[i]:
            lo = i + 1
            break

if lo <= P:
    print(rank)
else:
    print(-1)
