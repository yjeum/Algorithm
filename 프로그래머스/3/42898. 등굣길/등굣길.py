def solution(n, m, puddles):
    
    arr = [[0] * m for _ in range(n)]
    
    # 물에 잠긴 지역 표시(갈 수 없음)
    for pi, pj in puddles:
        arr[pi-1][pj-1] = -1

    # 시작점 표시
    arr[0][0] = 1    
    
    # 등교
    for i in range(n):
        for j in range(m):
            # 웅덩이인 경우 갈 수 있는 방법의 수는 0
            if arr[i][j] == -1:
                arr[i][j] = 0
            # 웅덩이가 아닌 경우 위와 왼쪽에서 올 수 있는 경우 확인
            else:
                if i - 1 >= 0:
                    arr[i][j] += arr[i-1][j]
                if j - 1 >= 0:
                    arr[i][j] += arr[i][j-1]
        
    return arr[n-1][m-1] % 1000000007
