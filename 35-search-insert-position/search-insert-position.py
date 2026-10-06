class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums) 
        ans=n
        left=0 
        right=n-1 
        while left<=right:
            mid=(left+right)//2 
            if nums[mid]>=target:
                ans=mid
                right=mid-1
            else:
                 left=mid+1
        return ans
            
                
