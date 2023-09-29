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
        size [y] += size[x]
    
    else:
        parent[y] = x
        size[x] += size[y]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
size = [1]*(n+1)

for i in range(m):
    cal, a, b = map(int, input().split())

    if cal == 0:
        union(a, b)
    else:
        find_set(a)
        find_set(b)

        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")