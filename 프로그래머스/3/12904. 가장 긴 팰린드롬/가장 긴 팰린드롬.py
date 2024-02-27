def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            word = s[i:j]
            if word == word[::-1]:
                answer = max(answer, (j - i))

    return answer