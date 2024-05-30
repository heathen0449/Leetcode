
items = [7, 3, 15, 1, 12, 4, 8, 5, 10, 6]
prices = [89, 24, 10, 67, 73, 11, 99, 38, 45, 19]
item_new = list(zip(items, prices))
capacity = 50
def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    # 计算最优解的物品列表
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selected_items

# 求解问题
max_value, selected_items = knapsack_01(item_new, capacity)

print(f"最大价值: {max_value}")
print("选择的物品 (重量, 价值):")
for weight, value in selected_items:
    print(f"重量 = {weight}, 价值 = {value}")