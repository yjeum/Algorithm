import heapq
N = int(input())

q = []

for i in range(N):
    i, j = map(int, input().split())
    heapq.heappush(q, (i, j))

for i in range(N):
    print(*heapq.heappop(q))