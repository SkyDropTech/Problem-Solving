class Solution:
    def longestCommonPrefix(self, nums: List[str]) -> str:
        res=""
        for j in range(len(nums[0])):
            curr=nums[0][j] 
            for i in range(1,len(nums)):
                if j>=len(nums[i]) or nums[i][j]!=curr:
                    return res 
                    exit() 
            res+=curr 
        return res

