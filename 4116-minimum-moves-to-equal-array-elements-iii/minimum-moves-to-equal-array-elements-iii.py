class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums) 
        suum=0
        n=len(nums)
        for i in range(n):
            suum+=maxi-nums[i] 
        return suum