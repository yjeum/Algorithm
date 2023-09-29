import sys
input = sys.stdin.readline

def par(par_lst, num_lst, c):
    if len(par_lst) == M:
        print(*par_lst)
        return
    
    c_n = 0
    for i in range(c, len(num_lst)):
        if c_n != num_lst[i]:
            par_lst.append(num_lst[i])
            c_n = num_lst[i]
            par(par_lst, num_lst, i)
            par_lst.pop()

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
par_lst = []

par(par_lst, num_lst, 0)