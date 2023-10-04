import sys
input = sys.stdin.readline

N = int(input())
bar_lst = [int(input()) for i in range(N)]
bar_lst.reverse()

cnt = 0
max_bar = 0
for i in bar_lst:
    if i > max_bar:
        max_bar = i
        cnt += 1
print(cnt)