import sys
input = sys.stdin.readline

def par(par_lst, num_lst, visited, c):
    if len(par_lst) == M:
        print(*par_lst)
        return
    
    c_n = 0
    for i in range(c+1, len(num_lst)):
        if visited[i]==0 and c_n != num_lst[i]:
            par_lst.append(num_lst[i])
            visited[i] = 1
            c_n = num_lst[i]
            par(par_lst, num_lst, visited, i)
            par_lst.pop()
            visited[i] = 0

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
par_lst = []
total = []
visited = [0]*N

par(par_lst, num_lst, visited, -1)