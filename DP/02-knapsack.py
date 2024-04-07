def knapSack(W, weights, profits, n): 
     
    # Making the result_sheet array 
    result_sheet = [0 for i in range(W+1)] 
 
    # Taking first i elements 
    for i in range(1, n+1): 
         
        # Starting from back, 
        # so that we also have data of 
        # previous computation when taking i-1 items 
        for w in range(W, 0, -1): 
            wt_in_list = weights[i-1]  # Weight from the list
            profit_in_list = profits[i-1]
            rem_wt = w - wt_in_list
            if wt_in_list <= w: 
                # Finding the maximum profitsue 
                result_sheet[w] = max(result_sheet[w], result_sheet[rem_wt] + profit_in_list) 
     
    # Returning the maximum profitsue of knapsack 
    return result_sheet[W] 
 
 
# Driver code 
if __name__ == '__main__': 
    profits = [2, 4, 7, 10]
    weights = [1, 3, 5, 7]
    capacity = 8
    n = len(profits) 
    print(knapSack(capacity, weights, profits, n)) 