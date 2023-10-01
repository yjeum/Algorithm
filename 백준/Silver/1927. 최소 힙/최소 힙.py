import sys
input = sys.stdin.readline

import heapq

N = int(input())
p = []

for i in range(N):
    num = int(input())
    if num == 0:
        if p:
            print(heapq.heappop(p))
        else:
            print(0)
    else:
        heapq.heappush(p, num)
