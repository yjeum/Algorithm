N = int(input())

A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

A_lst.sort()
min_score = 0

for i in range(N):
    min_score += A_lst[i] * max(B_lst)
    B_lst.remove(max(B_lst))
print(min_score)