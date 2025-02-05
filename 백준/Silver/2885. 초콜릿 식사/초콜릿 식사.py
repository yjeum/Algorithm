import sys

K = int(input())

# 최소 초콜릿 사이즈
min_size = 1
while min_size < K:
    min_size *= 2

# 최소 쪼개는 횟수
temp_size = min_size
remaining_size = K
temp_cnt = 0

if remaining_size == temp_size:
    print(min_size, 0)
    sys.exit()

while remaining_size > 0:
    temp_size //= 2
    temp_cnt += 1
    if remaining_size >= temp_size:
        remaining_size -= temp_size

print(min_size, temp_cnt)
