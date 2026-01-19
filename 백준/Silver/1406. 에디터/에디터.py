import sys
input = sys.stdin.readline

init_word = input().rstrip()
left_stack = [word for word in init_word]
right_stack = []
N = int(input())
for _ in range(N):
    action = input().rstrip()
    if action == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif action == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif action == "B":
        if left_stack:
            left_stack.pop()
    elif action[0] == "P":
        left_stack.append(action[2])

while right_stack:
    left_stack.append(right_stack.pop())
print("".join(left_stack))
