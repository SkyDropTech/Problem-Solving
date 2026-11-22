class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        ct=0 
        ans=0 
        for i in nums:
            ct+=1
            if i!=0:
                ct=0 
            
            ans+=ct 
        return ans