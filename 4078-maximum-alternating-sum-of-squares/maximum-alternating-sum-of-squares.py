class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums) 

        for i in range(n):
            nums[i]=nums[i]**2 
        suum1=0
        
        nums.sort() 
        total=sum(nums)
        for i in range(n//2):
            suum1+=nums[i] 

        suum2=total-suum1
        return suum2-suum1