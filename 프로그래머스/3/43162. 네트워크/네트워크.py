def DFS(now, visited, n, computers):
    visited[now] = 1
    for next in range(n):
        if computers[now][next] == 1 and visited[next] == 0:
            DFS(next, visited, n, computers)  
                
def solution(n, computers):            
    answer = 0
    visited = [0 for i in range(n)]
    for now in range(n):
        if visited[now] == 0:
            print("들어옴")
            DFS(now, visited, n, computers)
            answer += 1
        
    return answer