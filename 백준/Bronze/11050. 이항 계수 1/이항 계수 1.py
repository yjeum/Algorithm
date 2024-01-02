import sys

import math

input = sys.stdin.readline
n, k = map(int, input().split())
answer = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(answer)

