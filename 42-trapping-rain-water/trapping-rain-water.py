class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        left[0]=nums[0] 
        for i in range(1,n):
            left[i]=max(nums[i],left[i-1]) 
        right[n-1]=nums[n-1] 
        for i in range(n-2,-1,-1):
            right[i]=max(nums[i],right[i+1]) 
        water=0
        for i in range(n):
            water+=min(left[i],right[i])-nums[i]
        return water



