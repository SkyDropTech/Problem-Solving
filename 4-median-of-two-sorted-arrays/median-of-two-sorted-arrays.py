class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=nums1+nums2 
        nums.sort()
        n=len(nums) 
        left=0 
        right=n-1 
        k=1
        while k!=0:
            mid=(left+right)//2
            if n%2!=0:
                return nums[mid] 
            else:
                left=mid+1
                return (nums[left]+nums[mid])/2 
            k-=1 
        
        