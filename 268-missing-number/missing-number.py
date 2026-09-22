class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        for i,e in enumerate(nums):
            if i!=e:
                return i 
            if e==len(nums)-1:
                return e+1

