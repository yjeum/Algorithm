import sys

input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0
for size in sizes:
    if size % T == 0:
        t += size // T
    else:
        t += size // T + 1

print(t)
print(N // P, N % P)
