import sys
input = sys.stdin.readline

N = int(input())
cur_len, max_len, temp_val = 0, 0, 0

for _ in range(N):
    temp = list(map(int, input().split()))

    # 줄서는 경우
    if temp[0] == 1:
        cur_len += 1
        if max_len < cur_len:
            max_len = cur_len
            temp_val = temp[1]
        elif max_len == cur_len:
            temp_val = min(temp_val, temp[1])
    # 밥먹는 경우
    else:
        cur_len -= 1

print(max_len, temp_val)
