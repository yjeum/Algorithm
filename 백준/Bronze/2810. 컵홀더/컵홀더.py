import sys

input = sys.stdin.readline

N = int(input())
people = input()
print(min(N, people.count("S") + (people.count("L") // 2) + 1))
