import sys

input = sys.stdin.readline

dxdy = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dir = 0

N = int(input())
dir_list = list(input())

num_list = [(0, 0)]

cx, cy = 0, 0
min_cx, min_cy = 0, 0
max_cx, max_cy = 0, 0

for i in dir_list:
    if i == "F":
        cx, cy = cx + dxdy[dir][0], cy + dxdy[dir][1]
        num_list.append((cx, cy))
        min_cx, min_cy = min(min_cx, cx), min(min_cy, cy)
        max_cx, max_cy = max(max_cx, cx), max(max_cy, cy)
    elif i == "R":
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

arr_x = max_cx - min_cx + 1
arr_y = max_cy - min_cy + 1

maze = [["#"] * arr_y for _ in range(arr_x)]
for x, y in num_list:
    maze[x - min_cx][y - min_cy] = "."

for row in maze:
    print("".join(row))
