from collections import deque

didj = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def solution(land):

    N = len(land)
    M = len(land[0])
    
    cur = 1
    val = {}
    
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                
                cur += 1
                
                q = deque([(i, j)])
                land[i][j] = cur
                cnt = 1
                
                while q:
                    ci, cj = q.pop()
                    for di, dj in didj:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < M and land[ni][nj] == 1:
                            q.append((ni, nj))
                            land[ni][nj] = cur
                            cnt += 1
                
                
                val[cur] = val.get(cur, 0) + cnt
    
    temp_max = 0
    for j in range(M):
        temp_list = []
        for i in range(N):
            temp_list.append(land[i][j])
        
        set_list = list(set(temp_list))
        temp_val = 0
        for k in set_list:
            if k != 0:
                temp_val += val[k]
        temp_max = max(temp_val, temp_max)

        
    answer = temp_max
    return answer