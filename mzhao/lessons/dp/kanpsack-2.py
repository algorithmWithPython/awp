def knapsack1(bag_weight, item_weights, item_values):
    l = len(item_values)
    #base case dp[0][0]
    dp = [0]*(bag_weight+1)
    for i in range(1, l+1):
        for j in range(item_weights[i-1], bag_weight+1):
            dp[j] = max(dp[j], dp[j-item_weights[i-1]]+item_values[i-1])
    return dp[bag_weight]

