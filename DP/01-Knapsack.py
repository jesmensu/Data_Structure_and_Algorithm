def knapsack(capacity, weight, profits, n):
    result = [[0]*(capacity+1) for i in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            # if(i == 0 or w == 0):
            #     result[i][w] = 0
            # avl_wt = 
            avl_wt = weight[i-1]  # Weight from the list
            prev_wt = w - avl_wt
            if(avl_wt <= w):
                result[i][w] = max(profits[i-1] + result[i-1][prev_wt], result[i-1][w])
            else:
                result[i][w] = result[i-1][w]
    return result[n][capacity]



profits = [2, 4, 7, 10]
weights = [1, 3, 5, 7]
capacity = 8
ln = len(profits)
profits = knapsack(capacity, weights, profits, ln)
print(profits)