class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val=nums[0]
        suum=0
        n=len(nums)
        for i in range(n):
            suum+=nums[i] 
            max_val=max(max_val,suum)
            if suum<0:
                suum=0
        return max_val
        
