import sys
from collections import deque

input = sys.stdin.readline

def bfs(gp, start_spot, visited):
    q = deque([start_spot])

    visited[start_spot] = 0
    cnt = 1

    while q:
        
        now = q.popleft()
        order[now] = cnt

        cnt += 1
        gp[now].sort()

        for i in gp[now]:
            
            if visited[i] == -1:
                
                visited[i] = visited[now]+1
                q.append(i)

spot, edge, start_spot = map(int, input().split())

gp = [[] for _ in range(spot+1)]

for i in range(edge):
    start, end = map(int, input().split())
    gp[start].append(end)
    gp[end].append(start)


visited = [-1 for _ in range(spot+1)]
order = [-1 for _ in range(spot+1)]

bfs(gp, start_spot, visited)

sum = 0
for i in range(1, spot+1):
    if visited[i] != -1:
        sum += visited[i] * order[i]

print(sum)
