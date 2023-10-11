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


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]
    size = [1 for _ in range(N + 1)]

    for i in range(M):
        s, e = map(int, input().split())
        union(s, e)

    for i in range(N + 1):
        find_set(i)

    print(f"#{tc}", len(set(parent)) - 1)
