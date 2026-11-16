class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        n=len(nums) 
        for i in range(n):
            nums[i]=str(nums[i]) 
        ct=0 
        for i in nums:
            if len(i)%2==0:
                ct+=1 
        return ct