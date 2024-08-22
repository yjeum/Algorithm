import sys
import heapq

input = sys.stdin.readline


def makeB(A):
    while q:
        cnt, num = heapq.heappop(q)
        for temp in [int(num + "1"), int(num) * 2]:
            if temp > int(B):
                continue
            elif temp < int(B):
                heapq.heappush(q, (cnt + 1, str(temp)))
            else:
                return cnt + 1
    return -1


A, B = input().split()

q = [(1, A)]

print(makeB(A))
