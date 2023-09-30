# KRUSKAL사용
# 마지막 선만 이어주지 않으면 두개의 마을 생성
# 두 집의 경우 이어줄 필요 없음

import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    global cnt
    global sum_w

    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    cnt += 1
    sum_w += w
    if size[x] < size[y]:
        parent[x] = y
        size[y] += size[x]
    else:
        parent[y] = x
        size[x] += size[y]
    
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
size = [1]*(N+1)

edge = []
for _ in range(M):
    start, end, w = map(int, input().split())
    edge.append([start, end, w])
edge.sort(key=lambda x: x[2])

cnt = 0
sum_w = 0
for start, end, w in edge:
    union(start, end)

    if cnt == N-2:
        break

if N == 2:
    print(0)
else:
    print(sum_w)