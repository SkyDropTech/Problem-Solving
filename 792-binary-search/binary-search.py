class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums) 
        right=n-1 
        left=0 
        while left<=right:
            mid=(left+right)//2 
            if nums[mid]==target:
                return mid
                break 
            elif nums[mid]>target:
                right=mid-1 
            else:
                left=mid+1
        return -1
        