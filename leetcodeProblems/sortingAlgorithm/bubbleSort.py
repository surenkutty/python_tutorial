# assending order of array in bubble sort
arr = [3, 2, 4, 1, 5]

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            break
print(arr)      # [1, 2, 3, 4, 5]
            

# Bubble sort for descending order
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)  # Output: [5, 4, 3, 2, 1]


