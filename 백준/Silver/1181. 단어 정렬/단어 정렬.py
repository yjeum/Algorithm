import sys

input = sys.stdin.readline

N = int(input())
word_list = []

for i in range(N):
    word = input().strip()
    if (len(word), word) not in word_list:
        word_list.append((len(word), word))

word_list.sort()

for i in range(len(word_list)):
    print(word_list[i][1])
