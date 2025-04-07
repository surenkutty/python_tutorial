def removeduplicate(arr):
    result = []
    for i in range(len(arr)):
        duplicate = False
        for j in range(len(result)):
            if arr[i] == result[j]:
                duplicate = True
                break
        if not duplicate:
            result.append(arr[i])
    return result

arr= [1, 2, 3, 4, 5, 1, 2, 3]
print(removeduplicate(arr))