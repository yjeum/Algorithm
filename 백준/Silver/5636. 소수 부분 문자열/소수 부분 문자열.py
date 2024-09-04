import sys

input = sys.stdin.readline


def prime(temp):
    for i in range(2, temp):
        if temp % i == 0:
            return False
    return True


while True:
    origin = input().rstrip()

    if origin == "0":
        break
    else:
        answer = 0
        for i in range(len(origin)):
            for j in range(i + 1, len(origin) + 1):
                temp = origin[i:j]
                if len(temp) < 6 and prime(int(temp)):
                    answer = max(answer, int(temp))
    print(answer)
