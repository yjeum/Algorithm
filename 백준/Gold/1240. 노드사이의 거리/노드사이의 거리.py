import sys
from collections import deque
input = sys.stdin.readline


def dfs(s, target):
    stack = deque([(s, 0)])
    visited = [0] * (N + 1)
    visited[s] = 1

    while stack:
        c, w = stack.pop()
        if c == target:
            return w
        for n, temp_w in gp[c]:
            if visited[n] == 0:
                stack.append((n, w + temp_w))
                visited[n] = 1


N, M = map(int, input().split())

# 그래프 세팅
gp = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e, w = map(int, input().split())
    gp[s].append((e, w))
    gp[e].append((s, w))

for _ in range(M):
    u, v = map(int, input().split())
    print(dfs(u, v))
