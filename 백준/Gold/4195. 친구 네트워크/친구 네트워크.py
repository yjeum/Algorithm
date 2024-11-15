import sys

input = sys.stdin.readline


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x, y = find_set(x), find_set(y)

    if x == y:
        print(max(size[x], size[y]))
        return

    if size[x] < size[y]:
        parents[x] = y
        size[y] += size[x]
        print(size[y])
    else:
        parents[y] = x
        size[x] += size[y]
        print(size[x])


T = int(input())

for tc in range(T):

    N = int(input())
    parents = {}
    size = {}

    for network in range(N):
        friends = list(input().split())
        for friend in friends:
            if friend not in parents:
                parents[friend] = friend
                size[friend] = 1
        union(friends[0], friends[1])
