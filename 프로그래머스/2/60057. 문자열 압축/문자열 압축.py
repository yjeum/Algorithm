def solution(s):
    # 문자열 한글자씩 입력받기
    answer_lst = []
    
    # 1부터 문자열 길이만큼 잘라서 비교
    for i in range(1, len(s)+1):
        temp = ''
        # 첫 비교대상 지정
        before = s[:i]
        cnt = 1

        for j in range(i, len(s)+i, i):
            now = s[j:j+i]

            if before == now:
                cnt += 1
            else:
                if cnt != 1:
                    temp = temp + str(cnt) + str(before)
                else:
                    temp = temp + str(before)
                before = now
                cnt = 1
        answer_lst.append(len(temp))           
    return min(answer_lst)