def solution(friends, gifts):
    N = len(friends)
    
    # 주고받은 선물 갯수 배열
    arr = [[0] * N for _ in range(N)]
    # 선물 지수 배열
    point = {friend: 0 for friend in friends}
    
    for gift in gifts:
        give, receive = gift.split()
        arr[friends.index(give)][friends.index(receive)] += 1
        point[give] += 1
        point[receive] -= 1
    
    
    # 다음달 받을 선물 갯수 배열
    next_gift = [0] * N
    print(next_gift)
    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            if arr[i][j] > arr[j][i]:
                next_gift[i] += 1
            elif arr[i][j] < arr[j][i]:
                next_gift[j] += 1
            else:
                if point[friends[i]] > point[friends[j]]:
                    next_gift[i] += 1
                elif point[friends[i]] < point[friends[j]]:
                    next_gift[j] += 1
                    
                
    
    
    answer = max(next_gift)
    return answer