def countSort(arr):
    count=[0]*100
    for i in arr:
        count[i]+=1
    return count


arr=[1,2,3,5,6,1,3,2]
ans=countSort(arr)
print(ans)
        