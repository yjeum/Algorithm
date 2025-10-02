from itertools import combinations

def solution(n, q, ans):
    answer = 0
    num_list = [i for i in range(1, n+1)]
    
    # 사용하지 않는 숫자
    for i, val in enumerate(ans):
        if val == 0:
            for j in q[i]:
                if j in num_list:
                    num_list.remove(j)

    # 조합 만들기
    for comb in combinations(num_list, 5):
        # 시도한 조합
        for idx, q_list in enumerate(q):
            flg = True
            # 한개도 맞지 않았다면 이미 리스트에서 제외
            if ans[idx] != 0:
                cnt = 0
                for q_val in q_list:
                    if q_val in comb:
                        cnt += 1
                        if cnt > ans[idx]:
                            flg = False
                            break
                if cnt != ans[idx]:
                    flg = False
                    break
        if flg:
            answer += 1

    return answer