import sys
input = sys.stdin.readline

def dfs(start_x, start_y):

    stack = [(start_x, start_y)]
    visited[start_x][start_y] = 1

    while stack:
        x, y = stack.pop()

        if x == (N-1) and y == (N-1):
            return 'HaruHaru'
        
        k = arr[x][y]

        for didj in [[0,1],[1,0]]:
            ni, nj = x + didj[0]*k, y + didj[1]*k
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1
        
    return 'Hing'


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

print(dfs(0, 0))