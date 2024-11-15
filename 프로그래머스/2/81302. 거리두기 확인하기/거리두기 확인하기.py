didj = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def room(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                visited = [[0] * (5) for _ in range(5)]
                visited[i][j] = 1
                if recur(i, j, 0, place, visited) == False:
                    return False
    return True


def recur(ci, cj, depth, place, visited):
    
    if depth == 2:
        return True
    
    for di, dj in didj:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            if place[ni][nj] == 'P':
                return False
            elif place[ni][nj] == 'O':
                if not recur(ni, nj, depth + 1, place, visited):
                    return False
    return True
    
    

def solution(places):
    answer = []
    for t in range(5):
        if room(places[t]) == False:
            answer.append(0)
        else:
            answer.append(1)

    return answer
