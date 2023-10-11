def cost(n, cost_sum):
    global min_cost
    if min_cost < cost_sum:
        return
    if n >= 12:
        min_cost = min(min_cost, cost_sum)
        # print(tc, min_cost)
        return
    if cost_sum >= cost_lst[3]:
        min_cost = min(cost_lst[3], min_cost)
        return

    cost(n + 1, cost_sum + (cost_lst[0] * plan[n]))
    cost(n + 1, cost_sum + cost_lst[1])
    cost(n + 3, cost_sum + cost_lst[2])


T = int(input())
for tc in range(1, T + 1):
    cost_lst = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_cost = 1e9
    cost(0, 0)

    print(f"#{tc}", min_cost)
