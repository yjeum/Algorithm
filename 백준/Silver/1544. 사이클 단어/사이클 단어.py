import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
words = deque([input().rstrip() for _ in range(N)])
cnt = 0
while words:
    standard = words.popleft()
    standard *= 2
    len_words = len(words)
    for i in range(len_words):
        word = words.popleft()
        if len(word) * 2 != len(standard) or word not in standard:
            words.append(word)
    cnt += 1
print(cnt)
