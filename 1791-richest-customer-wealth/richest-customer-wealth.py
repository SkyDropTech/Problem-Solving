class Solution:
    def maximumWealth(self, nums: List[List[int]]) -> int:
        max_sum=0 
        n=len(nums)
        for i in range(n):
            ans=sum(nums[i])
            max_sum=max(max_sum,ans)
        return max_sum