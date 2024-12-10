def linearSearch(nums,target):
    arr=len(nums)-1
    for i in range(0,arr):
        if nums[i]==target:
            print(i)
            break
    else:
        print("number in non of the array")
    
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result=linearSearch(nums,target)
print(result)