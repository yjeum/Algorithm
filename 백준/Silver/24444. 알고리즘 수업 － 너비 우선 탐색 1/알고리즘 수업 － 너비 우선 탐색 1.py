import sys
from collections import deque

input = sys.stdin.readline

V, E, S = map(int, input().split())
gp = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    gp[start].append(end)
    gp[end].append(start)

for _ in range(V + 1):
    gp[_].sort()

q = deque([S])
visited = [0 for _ in range(V + 1)]
visited[S] = 1
cnt = 1

while q:
    cur = q.popleft()

    for next in gp[cur]:
        if visited[next] == 0:
            cnt += 1
            visited[next] = cnt
            q.append(next)

for i in range(1, V + 1):
    print(visited[i])
