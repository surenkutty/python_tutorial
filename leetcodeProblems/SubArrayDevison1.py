def birthday(s, d, m):
    count = 0
    n = len(s)
    
    # Loop to check subarrays of length m
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
            
    return count

# Example Input
s = [1, 2, 1, 3, 2]  # Chocolate bar pieces
d = 3  # Ron's birthday
m = 2  # Month (length of subarray)

# Call the function and print the result
result = birthday(s, d, m)
print(result)  # Expected Output: 2
