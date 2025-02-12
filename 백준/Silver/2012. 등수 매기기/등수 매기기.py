import sys
input = sys.stdin.readline

N = int(input())
lst = [0 for _ in range(N + 1)]
temp = []
for _ in range(N):
    num = int(input())
    if num <= N and lst[num] == 0:
        lst[num] = 1
    else:
        temp.append(num)

temp.sort()
temp_idx = 0
min_val = 0
for i in range(1, N + 1):
    if lst[i] == 0:
        min_val += abs(i - temp[temp_idx])
        temp_idx += 1
print(min_val)
