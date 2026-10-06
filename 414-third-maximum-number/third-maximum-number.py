class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=list(set(nums))
        nums=sorted(nums,reverse=True)
        if len(nums)==1 or len(nums)==2:
            return nums[0] 
        else:
            return nums[2]

