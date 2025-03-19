import sys
input = sys.stdin.readline

N = int(input())

std_word = input().rstrip()

# 기준 단어 기초 세팅
len_std = len(std_word)
std_dic = {}
for i in std_word:
    std_dic[i] = std_dic.get(i, 0) + 1

# 비슷한 단어 여부 확인
cnt = 0
for _ in range(N - 1):
    new_word = input().rstrip()

    if len_std - 1 <= len(new_word) and len(new_word) <= len_std + 1:
        copy_dic = std_dic.copy()
        temp = 0
        for j in new_word:
            if copy_dic.get(j):
                copy_dic[j] -= 1
            else:
                temp += 1
                if temp == 2:
                    break
        if temp != 2:
            remain_word = temp
            for v in copy_dic.values():
                remain_word += abs(v)
            if remain_word < 3:
                cnt += 1

print(cnt)
