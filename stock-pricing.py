def max_profit(prices):
    # Initialize an empty list to store calculated profit values
    list_values=[]

    
    for i in range(1,len(prices)):# Loop through each selling price
       
       for j in range(i):# Loop through each selling price
           
           # Calculate profit as the difference between selling price and the values before (buying prices)
           substracted_values=prices[i]-prices[j]
           list_values.append(substracted_values)
        
    # Initialize max_profit with the first profit in list_values, then iterate through all values to find the maximum profit
    max_profit = list_values[0]
    for i in range(len(list_values)):
        if max_profit < list_values[i]:
            max_profit = list_values[i]

    return max_profit
  
  






 
  

  