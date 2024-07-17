import sys

input = sys.stdin.readline

trees = {}
cnt = 0
while True:
    tree = input().rstrip()

    if tree == "":
        break

    trees[tree] = trees.get(tree, 0) + 1
    cnt += 1

tree_list = sorted(trees.keys(), key=lambda key: key)

for tree_name in tree_list:
    print(tree_name, format(round(trees[tree_name] * 100 / cnt, 4), ".4f"))
