class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n=len(nums) 
        tot=sum(nums) 
        diff=n*min(nums) 
        return tot-diff