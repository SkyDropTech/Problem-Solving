class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lst=[] 
        ans=-1
        n=len(nums)
        left=0 
        right=n-1 
        while left<=right:
            mid=(left+right)//2 
            if nums[mid]==target:
                ans=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        lst.append(ans)
        left=0 
        right=n-1 
        while left<=right:
            mid=(left+right)//2 
            if nums[mid]==target:
                ans=mid
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        lst.append(ans) 
        return lst


