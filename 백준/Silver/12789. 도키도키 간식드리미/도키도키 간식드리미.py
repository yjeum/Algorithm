import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
students = deque(list(map(int, input().split())))

next_num = 1
stack = []

while True:
    if students and students[0] == next_num:
        students.popleft()
        next_num += 1
    elif stack and stack[-1] == next_num:
        stack.pop()
        next_num += 1
    elif students:
        stack.append(students.popleft())
    elif stack:
        print("Sad")
        sys.exit()
    else:
        print("Nice")
        sys.exit()
