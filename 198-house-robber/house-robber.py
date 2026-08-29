class Solution:
    def rob(self, nums: List[int]) -> int:
        #Solved Using DP method
        n=len(nums) 
        dp=[0]*n 
        dp[0]=nums[0] 
        if n>1:
            dp[1]=max(dp[0],nums[1]) 
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]
        # n=len(nums)
        # sum1=0 
        # sum2=0 
        # for i in range(n):
        #     if i%2==0:
        #         sum2=max(sum2+nums[i],sum1)
        #     else:
        #         sum1=max(sum1+nums[i],sum2)
        # return max(sum1,sum2)