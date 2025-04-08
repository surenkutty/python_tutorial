def find_min_max(arr):
    if not arr:
        return None, None
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num<min_val:
            min_val = num
        if num>max_val:
            max_val = num
    return min_val, max_val

arr=[7, 2, 9, 4, 1, 6]
print("Minimum value:", find_min_max(arr)[0])
print("Maximum value:", find_min_max(arr)[1])