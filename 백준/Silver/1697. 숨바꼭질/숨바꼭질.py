import sys
input = sys.stdin.readline
from collections import deque


def bfs(start, end):
    visited = [0] * 100001
    q = deque()
    q.append((start, 0))

    while q:
        current, c_cnt = q.popleft()

        if current == end:
            return c_cnt

        operations = [current + 1, current - 1, current * 2]
        for operation in operations:
            if 0 <= operation <= 100000 and visited[operation] == 0:
                q.append((operation, c_cnt + 1))
                visited[operation] = 1


start, end = map(int, input().split())
print(bfs(start, end))
