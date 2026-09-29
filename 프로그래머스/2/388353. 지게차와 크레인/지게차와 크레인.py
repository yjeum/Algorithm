from collections import deque 
didj = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def solution(storage, requests):
    N, M = len(storage), len(storage[0])
    
    # 상하좌우 빈칸 제공
    board = [['' for _ in range(M + 2)]]
    for row in storage:
        board.append([''] + list(row) + [''])
    board.append(['' for _ in range(M + 2)])   
    
    cnt = 0
    for request in requests:
        
        target = request[0]
        
        # 크레인 사용하는 경우
        if len(request) == 2:
            for i in range(1, N + 1):
                for j in range(1, M + 1):
                    if board[i][j] == target:
                        board[i][j] = ''
                        cnt += 1
            continue
        
        # 지게차 사용하는 경우 > BFS
        visited = [[0] * (M + 2) for _ in range(N + 2)]
        visited[0][0] = 1
        q = deque([[0, 0]])
        to_remove = set()
        
        while q:
            ci, cj = q.popleft()
            
            for di, dj in didj:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < (N + 2) and 0 <= nj < (M + 2) and visited[ni][nj] == 0:
                    if board[ni][nj] == target:
                        to_remove.add((ni, nj))
                    elif board[ni][nj] == '':
                        q.append([ni, nj])
                        visited[ni][nj] = 1
                    
        
        cnt += len(to_remove)
        for ri, rj in to_remove:
            board[ri][rj] = ''

    return (N * M) - cnt