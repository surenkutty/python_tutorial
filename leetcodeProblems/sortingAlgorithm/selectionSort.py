def selectionSort(arr):
    for i in range(0,len(arr)-1):
        cur_min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[cur_min]:
                cur_min=j
        arr[i],arr[cur_min]= arr[cur_min],arr[i]
arr=[5,2,1,4,3]
selectionSort(arr)
print(arr)

arr=[5,2,1,4,3]
for i in range(1,len(arr)):
    if arr[i]<5:
        min1=i
        print(i)
        
print(arr)