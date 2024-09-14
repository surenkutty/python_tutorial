def sumtwonumber(num:list,target):
    x=len(num)
    print(x)
    for i in range(x):
        for j in range(i+1,x):
            if num[i]+num[j]==target:
                print([i,j])

sumtwonumber(num=[2,3,5,4,6],target=6)

# or
class Solution(object):
    def twoSum(self, nums, target):
        
        
        d = {}
        print(d)
        
        for i, num in enumerate(nums):
            
            diff = target - num
            print(diff)
            
         
            if diff in d:
                return [d[diff], i]
            
           
            d[num] = i

# Example usage
if __name__ == "__main__":
    
    solution = Solution()

   
    nums = [2, 7, 11, 15]
    target = 9

    result = solution.twoSum(nums, target)

    
    print(result)  # Output: [0, 1]
                
                 
            
              
        
        