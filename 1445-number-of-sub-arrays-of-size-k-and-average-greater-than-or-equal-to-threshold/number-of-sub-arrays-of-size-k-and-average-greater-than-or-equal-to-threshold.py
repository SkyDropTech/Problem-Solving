class Solution:
    def numOfSubarrays(self, nums: list[int], k: int, threshold: int) -> int:
        ct=0 
        n=len(nums) 
        ans=0
        for i in range(k):
            ans+=nums[i] 
        if ans//k>=threshold:
            ct+=1
        for i in range(n-k):
            ans=ans-nums[i]+nums[i+k] 
            if ans//k>=threshold:
                ct+=1 
        return ct
