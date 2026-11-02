class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums) 
        nums.sort() 
        suum=0
        m=n//2
        for i in range(n):
            suum+=abs(nums[m]-nums[i]) 
        return suum


