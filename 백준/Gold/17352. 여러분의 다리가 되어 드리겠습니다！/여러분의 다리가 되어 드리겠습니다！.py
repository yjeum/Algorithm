import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if size[x] < size[y]:
        parent[x] = y
        size[y] += size[x]
    else:
        parent[y] = x
        size[x] += size[y]


N = int(input())
parent = [i for i in range(N+1)]
size = [1]*(N+1)

for i in range(N-2):
    u, v = map(int, input().split())
    union(u, v)

for i in range(N+1):
    find_set(i)

print(*set(parent[1:]))
