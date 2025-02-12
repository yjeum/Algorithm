import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}
for _ in range(N):
    word = input().strip()

    if len(word) < M:
        continue
    words[word] = words.get(word, 0) + 1


word_lst = sorted(words.keys(), key=lambda x: (-words[x], -len(x), x))

for w in word_lst:
    print(w)
