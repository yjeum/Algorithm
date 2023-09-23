cnt = 0
arr = [[0]*100 for _ in range(100)]
for _ in range(4):
    s_x, s_y, e_x, e_y = map(int, input().split())
    for i in range(s_x,e_x):
        for j in range(s_y,e_y):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)