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

# 다른 사람 풀이 > all 사용해서 한번에 확인
# all과 any 사용법 익히기

# def can_place_mat(park, size):
#     # 공원의 행(row)와 열(col) 길이
#     rows, cols = len(park), len(park[0])

#     # park에서 주어진 size의 돗자리를 놓을 수 있는지 확인
#     for i in range(rows - size + 1):
#         for j in range(cols - size + 1):
#             # size x size 크기의 공간이 모두 '-1'인지 확인
#             if all(park[x][y] == '-1' for x in range(i, i + size) for y in range(j, j + size)):
#                 return True
#     return False

# def solution(mats, park):
#     # 돗자리 크기 내림차순으로 정렬
#     mats.sort(reverse=True)

#     # 각 돗자리 크기에 대해 놓을 수 있는지 확인
#     for size in mats:
#         if can_place_mat(park, size):
#             return size

#     return -1