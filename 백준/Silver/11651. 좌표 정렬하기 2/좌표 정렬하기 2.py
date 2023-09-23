import heapq
N = int(input())

q = []

for i in range(N):
    i, j = map(int, input().split())
    heapq.heappush(q, (j, i))

for i in range(N):
    j, i = heapq.heappop(q)
    print(i, j)