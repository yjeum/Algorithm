import sys

input = sys.stdin.readline

N = int(input())

N_lst = list(map(int, input().split()))

M = int(input())

M_lst = list(map(int, input().split()))

num_dic = {}
for i in N_lst:
    if i in num_dic:
        num_dic[i] += 1
    else:
        num_dic[i] = 1

for i in M_lst:
    if i in num_dic:
        print(num_dic[i], end=" ")
    else:
        print(0, end=" ")
