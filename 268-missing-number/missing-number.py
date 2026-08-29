class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi=max(nums) 
        for i in range(0,maxi+2):
            if i not in nums:
                return i 
                break 