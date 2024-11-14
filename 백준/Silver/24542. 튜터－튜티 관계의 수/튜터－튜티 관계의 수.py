import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if size[x] < size[y]:
        parent[x] = y
        size[y] += size[x]
    else:
        parent[y] = x
        size[x] += size[y]


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
size = [1] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

parent_dic = {}
for i in range(1, N + 1):
    parent[i] = find(i)
    parent_dic[parent[i]] = parent_dic.get(parent[i], 0) + 1

ans = 1
for temp in parent_dic.values():
    ans *= temp

print(ans % 1000000007)
