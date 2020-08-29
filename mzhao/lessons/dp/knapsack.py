def knapsack(bag_weight, item_weights, item_values):
    l = len(item_values)
    #base case dp[0][0]
    dp = [[0]*(bag_weight+1) for _ in range(l+1)]
    for i in range(1, l+1):
        for j in range(1, bag_weight+1):
            if item_weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_weights[i-1]]+item_values[i-1])
    return dp[l][bag_weight]

def knapsack1(bag_weight, item_weights, item_values):
    l = len(item_values)
    #base case dp[0][0]
    dp = [0]*(bag_weight+1)
    for i in range(1, l+1):
        for j in range(bag_weight, 0, -1):
            if item_weights[i-1] <= j:
                dp[j] = max(dp[j], dp[j-item_weights[i-1]]+item_values[i-1])
    return dp[bag_weight]

item_values = [6, 10, 12] 
item_weights = [1, 2, 3] 
bag_weight = 5
print(knapsack1(bag_weight, item_weights, item_values)) 



# w           1       2       3       4      5
# no item     0       0       0       0       0            
# item 1      6       6       6       6       6
# item 2      6       10      16      16      16     
# item 3      6       10      12      18      22     


