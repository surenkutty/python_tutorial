class Solution:
    def countAndSay(self,n):
        result = '1'
        for i in range(1,n):
            result = self.describe(result)
        return result
        
    def describe(self,s):
        result = []
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                result.append(str(count)+s[i-1])
                count=1
        result.append(str(count)+s[-1])
        return ''.join(result)

ans=Solution()
print(ans.countAndSay(4))  
