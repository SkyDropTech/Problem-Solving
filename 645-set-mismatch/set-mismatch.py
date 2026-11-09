class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums) 
        nums.sort()
        s=set(nums)
        x=0
        for i in range(1,n+1):
            if i not in s:
                x=i
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                return [nums[i],x]
                
         