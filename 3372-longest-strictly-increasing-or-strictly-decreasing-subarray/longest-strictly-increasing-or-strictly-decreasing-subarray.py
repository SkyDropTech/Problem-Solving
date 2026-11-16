class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums) 
        ct=1
        maxi1=1
        for  i in range(n-1):
            if nums[i]<nums[i+1]:
                ct+=1 
            else:
                ct=1
            maxi1=max(maxi1,ct) 
        ctt=1
        maxi2=1
        for  i in range(n-1):
            if nums[i]>nums[i+1]:
                ctt+=1 
            else:
                ctt=1
            maxi2=max(maxi2,ctt) 

        return max(maxi1,maxi2)

        