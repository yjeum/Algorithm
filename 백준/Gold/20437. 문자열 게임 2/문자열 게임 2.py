import sys
input = sys.stdin.readline


def find_len(word, N):

    max_len = -1
    min_len = 1e9

    alphabet = {}
    for idx, val in enumerate(word):
        alphabet[val] = alphabet.get(val, []) + [idx]

        len_cur = len(alphabet[val])
        if len_cur >= N:
            temp = alphabet[val][len_cur - 1] - alphabet[val][len_cur - N]
            min_len = min(min_len, temp)
            max_len = max(max_len, temp)

    if min_len == 1e9 or max_len == -1:
        print(-1)
    else:
        print(min_len + 1, max_len + 1)

    return


T = int(input())

for tc in range(T):
    word = input()
    N = int(input())

    find_len(word, N)
