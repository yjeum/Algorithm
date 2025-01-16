import sys
input = sys.stdin.readline

N = int(input())
skills = input().rstrip()
stack = {"L": 0, "S": 0}
cnt = 0

for skill in skills:
    if skill == "L" or skill == "S":
        stack[skill] = stack.get(skill, 0) + 1
    elif skill == "R":
        if stack["L"] > 0:
            stack["L"] -= 1
            cnt += 1
        else:
            break
    elif skill == "K":
        if stack["S"] > 0:
            stack["S"] -= 1
            cnt += 1
        else:
            break
    else:
        cnt += 1
print(cnt)
