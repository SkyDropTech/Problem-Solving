class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        suum=0
        for i in range(0,n,2):
            suum+=nums[i]
        return suum

