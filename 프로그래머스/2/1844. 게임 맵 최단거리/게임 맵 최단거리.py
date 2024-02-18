from collections import deque

def solution(maps):
    q = deque([(0, 0)]) # 시작점
    cnt = 0
    while q:
        ci, cj = q.popleft()
        cnt = maps[ci][cj]  # 현재 위치까지의 거리
        
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]):
                if maps[ni][nj] == 1:
                    maps[ni][nj] = cnt + 1  # 다음 위치까지의 거리
                    q.append((ni, nj))
    
    return -1 if maps[len(maps)-1][len(maps[0])-1] == 1 else maps[len(maps)-1][len(maps[0])-1]
