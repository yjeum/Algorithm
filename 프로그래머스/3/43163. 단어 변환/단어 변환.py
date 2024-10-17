answer = 1e9

def backtracking(cur, visited, temp_cnt, target, words):
    global answer
    
    if temp_cnt > answer:
        return
    
    if cur == target:
        answer = min(answer, temp_cnt)
        return answer
    
    for i in range(len(words)):
        if visited[i] == False:
            check = 0
            for j in range(len(cur)):
                if cur[j] != words[i][j]:
                    check += 1
            if check == 1:
                visited[i] = True
                backtracking(words[i], visited, temp_cnt + 1, target, words)
                visited[i] = False
    
    return answer

def solution(begin, target, words):
    global answer
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    answer = backtracking(begin, visited, 0, target, words)
    
    return answer