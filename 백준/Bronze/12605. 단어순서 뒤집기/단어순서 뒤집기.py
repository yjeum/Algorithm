import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N + 1):
    lst = list(input().split())
    print(f"Case #{i}:", *lst[::-1])
