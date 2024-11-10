def fractionalKnapsack(W, arr, n):
    # Sort items based on value/weight ratio in descending order
    arr.sort(key=lambda x: x[1] / x[0], reverse=True)  # x[1] = value, x[0] = weight
    
    curWeight = 0
    finalvalue = 0.0
    
    for i in range(n):
        weight, value = arr[i]  # Unpack each item into weight and value
        
        if curWeight + weight <= W:
            curWeight += weight
            finalvalue += value
        else:
            remain = W - curWeight
            finalvalue += value / weight * remain
            break
            
    return finalvalue

if __name__ == "__main__":
    # List of items (weight, value)
    arr = [(10, 60), (20, 100), (30, 120)]  # Example items with weight and value
    W = 50  # Maximum capacity of knapsack
    n = len(arr)  # Number of items
    
    result = fractionalKnapsack(W, arr, n)
    print(result)  # Output the maximum value that can be obtained
