def par(n, m, par_lst, c):
    if len(par_lst) == m:
        print(*par_lst)
        return
    
    for i in range(1, n+1):
        if c <= i:
            par_lst.append(i)    
            par(n, m, par_lst, i)
            par_lst.pop()

N, M = map(int, input().split())
par_lst = []
par(N, M, par_lst, 0)
