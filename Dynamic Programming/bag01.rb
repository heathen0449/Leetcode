def bag_01(prices, weights, capacity)
  dp = Array.new(capacity + 1 , 0)
  prices.size.times do |i|
    capacity.downto(weights[i]) {|j| dp[j] = [dp[j], dp[j-weights[i]] + prices[i]].max}
  end
  dp[capacity]
end

items = [
    [7, 89],  # 物品 1: 重量 = 7, 价值 = 89
    [3, 24],  # 物品 2: 重量 = 3, 价值 = 24
    [15, 10], # 物品 3: 重量 = 15, 价值 = 10
    [1, 67],  # 物品 4: 重量 = 1, 价值 = 67
    [12, 73], # 物品 5: 重量 = 12, 价值 = 73
    [4, 11],  # 物品 6: 重量 = 4, 价值 = 11
    [8, 99],  # 物品 7: 重量 = 8, 价值 = 99
    [5, 38],  # 物品 8: 重量 = 5, 价值 = 38
    [10, 45], # 物品 9: 重量 = 10, 价值 = 45
    [6, 19]   # 物品 10: 重量 = 6, 价值 = 19
]

capacity = 50  # 背包容量为 50
price = []
weight = []
items.each do |item|
  weight << item[0]
  price << item[1]
end
pp weight, price
pp bag_01(price, weight, capacity)
