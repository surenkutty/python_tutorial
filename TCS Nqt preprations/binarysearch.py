def binarysearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[1,2,3,4,5]
target=4
result=binarysearch(arr,target)
if result!=-1:
    print(f"Element found at index {result}")   
else:
    print("Element not found in array")