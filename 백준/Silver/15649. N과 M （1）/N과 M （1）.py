# 순열 함수 사용하여 풀이

from itertools import combinations, permutations

n,m = list(map(int,input().split()))

numbers = [x+1 for x in range(n)]
permutation = list(permutations(numbers, m))
for answer in permutation:
    print(" ".join(map(str, answer)))