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

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
size = [1]*(N+1)

for i in range(M):
    u, v = map(int, input().split())
    union(u, v)

num_dic = {}
for i in range(N+1):
    parent[i] = find_set(i)
    num_dic[parent[i]] = num_dic.get(parent[i], 0) + 1

res = 1
for value in num_dic.values():
    res *= value

print(res%1000000007)