import sys

input = sys.stdin.readline


def upperbound(h, trees):
    lo = 0
    hi = max(trees)

    while lo + 1 < hi:
        mid = (hi + lo) // 2

        sum_tree = 0
        # print("####", mid, lo, hi)

        for tree in trees:
            if (tree - mid) > 0:
                sum_tree += tree - mid
            # print(mid, lo, hi, sum_tree)

            if sum_tree >= h:
                lo = mid
                break

        if sum_tree < h:
            hi = mid

    return lo


N, M = map(int, input().split())
trees = list(map(int, input().split()))
# trees = sorted(trees, reverse=True)

print(upperbound(M, trees))
