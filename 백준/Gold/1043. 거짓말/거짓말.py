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

def union_ori(list):
    if list[0] == 1:
        return
    else:
        for i in range(2, list[0]+1):
            union(list[1], list[i])


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
size = [1]*(N+1)

truth = list(map(int, input().split()))

if truth[0] == 0:
    print(M)

else:
    for i in range(truth[0]):
        union_ori(truth)

    arr = [list(map(int, input().split())) for _ in range(M)]

    for i in range(M):
        union_ori(arr[i])

    for i in range(N+1):
        find_set(i)

    cnt = 0
    for i in range(M):
        for j in range(1, arr[i][0]+1):
            if parent[arr[i][j]] != parent[truth[1]]:
                cnt += 1
                break

    print(cnt)