import sys

input = sys.stdin.readline

H, N = map(int, input().split())
hands = []

for i in range(1, N + 1):
    h1, h2 = map(int, input().split())
    hands.append((h1, i))
    hands.append((h2, i))
hands.sort()
print(hands[(H - 1) % (N * 2)][1])
