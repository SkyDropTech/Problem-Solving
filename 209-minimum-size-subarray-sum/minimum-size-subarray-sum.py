class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        suum=0
        mini=float('inf')
        for r in range(len(nums)):
            suum+=nums[r]
            while suum>=target:
                mini=min(mini, r-l+1)
                suum-=nums[l]
                l+=1

        if mini==float('inf'):
            return 0
        return mini

