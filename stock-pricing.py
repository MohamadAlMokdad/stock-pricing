def max_profit(prices):
    max_diff = 0
    
    # Outer loop to iterate through each price starting from the second element 
    for i in range(1, len(prices)):
        # Inner loop to iterate over all previous prices before the current price at index 'i'
        for j in range(i):
            # Calculate the difference between the price at index 'i' and the price at index 'j'
           
            if prices[i] - prices[j] > max_diff:
                max_diff = prices[i] - prices[j]
    
    # Return the maximum profit found
    return max_diff


