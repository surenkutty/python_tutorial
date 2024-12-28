
def minMax(arr):
    totalsum=0
    min_elem=arr[0]
    max_elem=arr[0]
    
    for i in arr:
       totalsum+=i
       if i<min_elem:
           min_elem=i
       if i>max_elem:
           max_elem=i
    min_sum=totalsum-min_elem
    max_sum=totalsum-max_elem
     # Print the results
    print(min_sum, max_sum)

# Example usage
arr = [1, 3, 5, 7, 9]
minMax(arr)