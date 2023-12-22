import sys

input = sys.stdin.readline

direction = 0

for i in range(10):
    change_direction = int(input())
    direction += change_direction

direction_list = ["N", "E", "S", "W"]
print(direction_list[direction % 4])
