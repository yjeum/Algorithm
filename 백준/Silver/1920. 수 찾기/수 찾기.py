import sys
input = sys.stdin.readline


def binary(target):

    left, right = 0, len(N_lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if target < N_lst[mid]:
            right = mid - 1
        elif target == N_lst[mid]:
            print(1)
            return True
        else:
            left = mid + 1
    print(0)
    return False


N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

N_lst.sort()

for target in M_lst:
    binary(target)
