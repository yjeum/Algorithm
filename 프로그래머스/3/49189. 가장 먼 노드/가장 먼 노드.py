from collections import deque

def BFS(start, visited, gp):
    
    q = deque([1])
    visited[1] = 1
    
    while q:
        now = q.popleft()
        
        for next in gp[now]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = visited[now] + 1
                

def solution(n, edge):
    
    # 1. visited 만들어주기
    visited = [0] * (n + 1)
    
    # 2. gp 만들어주기
    gp = [[] for _ in range(n + 1)]
    
    for start, end in edge:
        gp[start].append(end)
        gp[end].append(start)
    
    # 3. BFS
    BFS(1, visited, gp)

    # 4. visited 확인하여 갯수 count
    max_cnt = max(visited)
    answer = visited.count(max_cnt)

    return answer