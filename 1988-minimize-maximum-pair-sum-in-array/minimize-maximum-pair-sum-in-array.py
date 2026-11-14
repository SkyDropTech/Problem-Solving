class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort() 
        n=len(nums)
        j=n-1 
        i=0 
        maxi=0
        while i<j:
            ans=nums[i]+nums[j]
            maxi=max(maxi,ans) 
            i+=1 
            j-=1 
        return maxi