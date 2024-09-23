import sys

input = sys.stdin.readline

string = input().rstrip()
target = input().rstrip()

last_target = target[-1]
stack = []

# string을 돌면서 마지막 글자가 일치할 경우 확인
for cur in string:
    stack.append(cur)
    if cur == last_target:
        if "".join(stack[len(stack) - len(target) :]) == target:
            for _ in range(len(target)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
