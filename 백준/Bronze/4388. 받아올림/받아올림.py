import sys

input = sys.stdin.readline

while True:
    num_list = list(input().split())

    num1 = max(num_list)
    num2 = min(num_list)

    if num1 == "0" and num2 == "0":
        break

    num2 = (len(num1) - len(num2)) * "0" + num2

    round_up = 0
    cnt = 0
    for i in range(len(num1) - 1, -1, -1):
        if (round_up + int(num1[i]) + int(num2[i])) >= 10:
            round_up = 1
            cnt += 1
        else:
            round_up = 0
    print(cnt)
