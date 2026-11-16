class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        x=len(nums)
        i=0
        ct=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                ct+=1
                i+=1
            else:
                i+=2 
        if (len(nums)-ct)%2!=0:
            ct+=1 
        return ct