class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums) 
        nums.sort()
        for i in range(1,n+1):
            if i not in nums:
                x=i
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i+1]=x
                return [nums[i],nums[i+1]]
                break 
         