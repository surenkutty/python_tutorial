class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            elif target<nums[m]:
                r = m - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 7
    result = solution.search(nums, target)
    print(result) 

    #   or
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
