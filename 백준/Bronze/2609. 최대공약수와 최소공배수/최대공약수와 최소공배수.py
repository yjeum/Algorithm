import sys

input = sys.stdin.readline

# 유클리드 호제법
# a, b = b, a % b 에서 a % b가 0이 되는 순간의 b가 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수
# a와 b의 곱을 최대 공약수로 나눈 값
def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))


# 내장함수 사용한 풀이

# import math

# a,b = map(int,input().split())

# print(math.gcd(a,b))
# print(math.lcm(a,b))
