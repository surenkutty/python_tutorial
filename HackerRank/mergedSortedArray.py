class Solution:
    def merge(self, nums1, m, nums2, n):
        i=m-1
        j=n-1
        k=m+n-1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
            
            #or
        '''       
        last = m + n - 1
        
        
        # Merge from the end
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # Copy remaining elements from nums2 if any
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
            '''

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 5]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
