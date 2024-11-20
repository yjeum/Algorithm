import sys

input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

num_dic = {}
for number in N_lst:
    num_dic[number] = num_dic.get(number, 0) + 1
    
for i in M_lst:
    if i in num_dic:
        print(1)
    else:
        print(0)
