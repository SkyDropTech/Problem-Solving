class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left=[] 
        right=[] 
        mid=[] 
        nums.append("x")
        n=len(nums)
        for i in range(n-1):
            if nums[i]<pivot:
                left.append(nums[i]) 
            elif nums[i]>pivot:
                right.append(nums[i]) 
            elif nums[i]==pivot:
                mid.append(nums[i]) 
        return left+mid+right