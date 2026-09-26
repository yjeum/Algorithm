def solution(mats, park):
    # 공원 크기
    n, m = len(park), len(park[0])

    # 돗자리 크기 정렬
    mats.sort(reverse = True)

    for mat in mats:
        # 만약 돗자리가 공원보다 더 큰 경우 제외
        if min(n, m) < mat:
            continue
            
        # 시작점
        for i in range(n - mat + 1):
            for j in range(m - mat + 1):
                # 자리가 비어있다면 탐색 시작
                if park[i][j] == "-1":
                    flg = True
                    for k in range(i, i + mat):
                        for l in range(j, j + mat):
                            if park[k][l] == "-1":
                                continue
                            # 돗자리를 놓을 수 없는 경우
                            flg = False
                            break
                        if flg == False:
                            break
                    if flg == True:
                        return mat
    
    return -1