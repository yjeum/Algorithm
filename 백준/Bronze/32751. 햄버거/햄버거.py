import sys
input = sys.stdin.readline

N = int(input())
ingre = list(map(int, input().split()))
ingre_str = ["a", "b", "c", "d"]
ingre_dic = {}
for i in range(4):
    ingre_dic[ingre_str[i]] = ingre[i]

hambur = input().rstrip()

if hambur[0] != "a" or hambur[-1] != "a":
    print("No")
    sys.exit()
else:
    ingre_dic["a"] -= 1

before = hambur[0]
for cur in hambur[1:]:
    if before != cur and ingre_dic[cur] > 0:
        before = cur
        ingre_dic[cur] -= 1

    else:
        print("No")
        sys.exit()
print("Yes")
