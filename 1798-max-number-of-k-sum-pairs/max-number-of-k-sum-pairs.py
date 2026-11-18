class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n=len(nums) 
        nums.sort() 
        i=0 
        ct=0
        j=n-1
        while i<j:
            if nums[i]+nums[j]==k:
                ct+=2  
                i+=1 
                j-=1 
            elif nums[i]+nums[j]>k:
                j-=1 
            else:
                i+=1 
        return ct//2


    