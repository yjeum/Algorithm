import sys

input = sys.stdin.readline

N, X = map(int, input().split())
nums = list(map(int, input().split()))

temp = sum(nums[:X])
max_val = temp
cnt = 1
for i in range(X, N):
    temp -= nums[i - X]
    temp += nums[i]
    if max_val == temp:
        cnt += 1
    elif max_val < temp:
        cnt = 1
        max_val = temp

if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(cnt)
