import sys


input = sys.stdin.readline

A, B, V = map(int, input().split())
if (V - A) % (A - B) != 0:
    cnt = (V - A) // (A - B) + 1
else:
    cnt = (V - A) // (A - B)
print(cnt + 1)
