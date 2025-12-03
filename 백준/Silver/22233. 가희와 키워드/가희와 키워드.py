import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keywords = {}
for _ in range(N):
    keywords[input().rstrip()] = 1

cnt = N

for _ in range(M):
    words = list(input().rstrip().split(","))
    for word in words:
        if word in keywords.keys() and keywords[word] == 1:
            keywords[word] = 0
            cnt -= 1

    print(cnt)
