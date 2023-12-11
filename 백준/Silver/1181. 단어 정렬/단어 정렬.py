import sys

input = sys.stdin.readline

N = int(input())
word_list = []

for i in range(N):
    word = input().strip()
    # 지금은 튜플을 사용하여 풀었지만, 
    # 길이를 키값으로 가진 딕셔너리로 풀어도 좋을것 같음
    if (len(word), word) not in word_list:
        word_list.append((len(word), word))

word_list.sort()

for i in range(len(word_list)):
    print(word_list[i][1])
