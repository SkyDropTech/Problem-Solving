class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        number=nums[0] 
        n=len(nums)
        max_val=-1 
        for i in range(n):
            if nums[i]>number:
                max_val=max(max_val,nums[i]-number) 
            number=min(number,nums[i])
        return max_val