T = int(input())
p = [0 for _ in range(1001)]

max_val = 0
max_val_idx = 0
max_idx = 0

for _ in range(T):
    x, y = map(int, input().split())
    p[x] = y

    if max_val < y:
        max_val, max_val_idx = y, x
    if max_idx < x:
        max_idx = x

c_m = 0
sum_area = 0
for i in range(max_val_idx+1):
    if c_m < p[i]:
        c_m = p[i]
    sum_area += c_m

c_m = 0
for i in range(max_idx, max_val_idx, -1):
    if c_m < p[i]:
        c_m = p[i]
    sum_area += c_m

print(sum_area)