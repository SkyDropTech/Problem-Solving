class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        n=len(nums) 
        lst=[0]*n 
        maxi=0
        for i in range(n):
            if nums[i]>maxi:
                maxi=nums[i]
            ans=nums[i]+maxi 
            lst[i]=ans 
        suum=0
        for i in range(len(lst)):
            suum+=lst[i]
            lst[i]=suum 
        return lst

