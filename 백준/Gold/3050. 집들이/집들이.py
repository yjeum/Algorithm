import sys
input = sys.stdin.readline

R, C = map(int, input().split())

arr = [input().rstrip() for _ in range(R)]

height = [0] * C
max_cnt = 0

for i in range(R):
    # 현재 행 높이 갱신
    for j in range(C):
        if arr[i][j] == ".":
            height[j] += 1
        else:
            height[j] = 0

    # 각 행에 대해 왼쪽에 더 낮은 수 위치 찾기
    left_stack = []
    left_idx = [-1] * C
    for k in range(C):
        while left_stack and height[left_stack[-1]] >= height[k]:
            left_stack.pop()
        if left_stack:
            left_idx[k] = left_stack[-1]
        left_stack.append(k)

    # 각 행에 대해 오른쪽에 더 낮은 수 위치 찾기
    right_stack = []
    right_idx = [C] * C
    for l in range(C - 1, -1, -1):
        while right_stack and height[right_stack[-1]] >= height[l]:
            right_stack.pop()
        if right_stack:
            right_idx[l] = right_stack[-1]
        right_stack.append(l)

    # 둘레 구하기
    for m in range(C):
        if height[m] != 0:
            cnt = 2 * (right_idx[m] - left_idx[m] - 1 + height[m]) - 1
            max_cnt = max(cnt, max_cnt)

print(max_cnt)