import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
num_lst = list(map(int, input().split()))

left_max = max(num_lst[: L - 1], default=0)
middle_min = min(num_lst[L - 1 : R])
middle_max = max(num_lst[L - 1 : R])
right_min = min(num_lst[R:], default=1e9)

if left_max <= middle_min and middle_max <= right_min:
    print(1)
else:
    print(0)
