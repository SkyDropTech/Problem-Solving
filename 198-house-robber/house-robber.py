class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=0 
        sum2=0 
        for i in range(n):
            if i%2==0:
                sum2=max(sum2+nums[i],sum1)
            else:
                sum1=max(sum1+nums[i],sum2)
        return max(sum1,sum2)