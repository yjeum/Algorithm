from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

q = deque()
q.append((0,0))

while q:
    c_i, c_j = q.popleft()
    
    for didj in [[0,1],[0,-1],[1,0],[-1,0]]:
        ni, nj = c_i + didj[0], c_j + didj[1]

        if 0<=ni<N and 0<=nj<M and maze[ni][nj] == '1':
            q.append((ni,nj))
            maze[ni][nj] = maze[c_i][c_j] + '1'

print(len(maze[N-1][M-1]))
