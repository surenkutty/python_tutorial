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

