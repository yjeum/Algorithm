import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(stack):
    global cnt
    cur = stack.pop()

    if visited[cur] == 0:
        cnt += 1
        visited[cur] = cnt
        for next in gp[cur]:
            if visited[next] == 0:
                stack.append(next)
                DFS(stack)


N, M, R = map(int, input().split())

# 무방향 그래프 생성
gp = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    gp[u].append(v)
    gp[v].append(u)

for i in range(1, N + 1):
    gp[i].sort()

# 시작점으로부터 거리 계산
visited = [0] * (N + 1)
cnt = 0
DFS([R])

for i in range(1, N + 1):
    print(visited[i])
