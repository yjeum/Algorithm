def solution(n, words):
    cnt, person = 0,0

    used = [words[0]]
    before = words[0]
    
    for i in range(1,len(words)):
        if words[i] not in used and words[i][0] == before[-1]:
            used.append(words[i])
            before = words[i]
        else:
            cnt = (i % n) + 1
            person = (i // n) + 1
            break
    
    return [cnt, person]