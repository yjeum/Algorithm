import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque([(1, 0)])  # (cur, clip)
visited = [[False] * 1001 for _ in range(1001)]
cnt = 0

while q:
    cur, clip = q.popleft()

    if cur == N:
        print(visited[cur][clip])
        break

    arr = [(cur, cur), (cur + clip, clip), (cur - 1, clip)]

    for c, v in arr:
        if 0 < c < 1001 and 0 <= v < 1001 and visited[c][v] == False:

            q.append((c, v))
            visited[c][v] = visited[cur][clip] + 1
