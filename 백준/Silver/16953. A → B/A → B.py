import sys
import heapq

input = sys.stdin.readline


def makeB(A):
    while q:
        cnt, num = heapq.heappop(q)
        for temp in [num * 10 + 1, num * 2]:
            if temp > B:
                continue
            elif temp < B:
                heapq.heappush(q, (cnt + 1, temp))
            else:
                return cnt + 1
    return -1


A, B = map(int, input().split())

q = [(1, A)]

print(makeB(A))
