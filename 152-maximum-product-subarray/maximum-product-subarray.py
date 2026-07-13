class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0] 
        mini=nums[0] 
        ans=nums[0] 
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxi,mini=mini,maxi 

            maxi=max(nums[i],nums[i]*maxi)
            mini=min(nums[i],nums[i]*mini) 
            ans=max(maxi,ans) 
        return ans 
            


