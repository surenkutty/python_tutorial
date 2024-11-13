def mergeSort(arr):
    if len(arr)>1:
        middle=len(arr)//2
        left=arr[:middle]
        right=arr[middle:]
        print(left)
        print(right)
        
        mergeSort(left)
        mergeSort(right)
        i=0 #left
        j=0 #right
        
        k=0
        while i<len(left)and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i +=1
            else:
                arr[k]=right[j]
                j +=1
            k +=1
        while i<len(left):
            arr[k]=left[i]
            k +=1
            i +=1
        while j<len(right):
            arr[k]=right[j]
            k +=1
            j +=1
arr=[5,3,1,2,4]
mergeSort(arr)
print(arr)    
        