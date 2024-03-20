import sys

input = sys.stdin.readline

def DFS(gp, visited, start):
    visited[start] = 1
    for end in gp[start]:
        if visited[end] == 0:
            DFS(gp, visited, end)



u, v = map(int, input().split())
gp = [[] for _ in range(u + 1)]

visited = [0 for _ in range(u+1)]

for i in range(v):
    start, end = map(int, input().split())
    gp[start].append(end)
    gp[end].append(start)

count = 0
for i in range(1, u+1):
    if visited[i] == 0:
        DFS(gp, visited, i)
        count += 1

print(count)