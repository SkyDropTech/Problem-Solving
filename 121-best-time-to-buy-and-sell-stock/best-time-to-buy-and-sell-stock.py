class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        n=len(nums)
        mini=nums[0] 
        max_val=0 
        for i in range(1,n):
            if nums[i]>mini:
                max_val=max(max_val,nums[i]-mini)
            mini=min(mini,nums[i])
        return max_val
