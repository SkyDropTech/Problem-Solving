class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n=len(nums) 
        ans=0
        mn=nums[0] 
        for i in range(n):
            if nums[i]>mn:
                ans=max(ans,nums[i]-mn) 
            mn=min(mn,nums[i])
        return ans