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


# or

def selection(arr):
    
    n=len(arr)
    print("hrllo",n)
    for i in range(n):
        mn=i
        print("ini",mn)
        for j in range(i+1,n):
            if arr[j]<arr[mn]:
                mn=j
                print(mn)
        arr[i],arr[mn]=arr[mn],arr[i]
    return arr
    
    
if __name__=="__main__":
    arr=[8,4,3,2,5,1]
    ans=selection(arr)
    print(ans)