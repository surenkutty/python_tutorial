def findMedian(arr):
    arr.sort()  # Sort the array
    mid = len(arr) // 2  # Find the middle index
    return arr[mid]  # Return the middle element
arr = [5, 3, 1, 2, 4]
print(findMedian(arr))  