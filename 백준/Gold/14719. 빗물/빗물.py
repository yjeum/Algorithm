import sys

input = sys.stdin.readline

H, W = map(int, input().split())
walls = list(map(int, input().split()))

arr = [[0] * (W) for _ in range(H)]

# arr에 wall 설치
for j in range(W):
    wall = walls[j]
    for i in range(H):
        if wall == i:
            break
        else:
            arr[i][j] = 1

# 빗물 count
water = 0
for i in range(H):
    temp = 0
    flag = False
    for j in range(W):
        if flag == True and arr[i][j] == 0:
            temp += 1
        elif flag == False and arr[i][j] == 1:
            flag = True
        elif flag == True and arr[i][j] == 1:
            water += temp
            temp = 0

print(water)
